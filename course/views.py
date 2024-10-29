from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from .models import Course


@login_required
def course_list(request):
    available_courses = Course.objects.exclude(user_courses__user=request.user)
    return render(
        request,
        'course_list.html',
        context={'available_courses': available_courses},
    )


@login_required
def course_details(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(
        request,
        'course_details.html',
        context={'course': course},
    )
