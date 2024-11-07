from coursera.test import TestCase

from .factories import CourseFactory
from user.tests.factories import UserFactory


class CourseListTestCase(TestCase):

    def test_list_view_redirects_to_login_for_not_logged_in_user(self):
        response = self.client.get('/courses/', follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.wsgi_request.path, '/login/')

    def test_list_view_returns_list_of_not_buyed_courser_to_user(self):
        courses = CourseFactory.create_batch(size=3)
        expected_available_courses = CourseFactory.create_batch(size=2)

        user = UserFactory(courses=courses)

        self.set_user(user)

        response = self.client.get('/courses/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'course_list.html')

        self.assertEqual(len(response.context['available_courses']), 2)
        self.assertListEqual(
            [course.pk for course in response.context['available_courses']],
            [course.pk for course in expected_available_courses]
        )

    def test_details_view_redirects_to_login_for_not_logged_in_user(self):
        response = self.client.get('/courses/1/', follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.wsgi_request.path, '/login/')

    def test_details_view_returns_404_if_course_does_not_exist(self):
        self.set_user(UserFactory())
        response = self.client.get('/courses/1000/', follow=True)

        self.assertEqual(response.status_code, 404)

    def test_details_view_redirects_to_user_course_if_course_bought_by_user(self):
        course = CourseFactory()
        self.set_user(UserFactory(courses=[course]))

        response = self.client.get(f'/courses/{course.pk}/', follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.wsgi_request.path,
            f'/user_courses/{course.pk}/'
        )

    def test_details_view_returns_course_details_to_user(self):
        course = CourseFactory()
        self.set_user(UserFactory())

        response = self.client.get(f'/courses/{course.pk}/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'course_details.html')
        self.assertEqual(response.context['course'], course)
