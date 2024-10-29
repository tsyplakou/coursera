from django.test import TestCase


class CourseListTestCase(TestCase):
    def test_list_view_returns_302_for_not_logged_in_user(self):
        response = self.client.get('/courses/')
        self.assertEqual(response.status_code, 302)
