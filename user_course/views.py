from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect

from course.models import Course


@login_required
def user_course_details(request, pk):
    course = get_object_or_404(Course, pk=pk)
    user_course = course.user_courses.filter(user=request.user).first()

    if not user_course:
        return redirect('course_details', pk=pk)

    achievements = request.user.achievements.filter(course=course).order_by('-score')
    return render(
        request,
        'user_course_details.html',
        context={
            'course': course,
            'user_course': user_course,
            'achievements': achievements,
        },
    )
