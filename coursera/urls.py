"""
URL configuration for coursera project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from user.views import login_view, logout_view, register_view
from course.views import course_list, course_details
from user_course.views import user_course_details, course_purchase
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    # Add your URL patterns here.
    path('', index, name='index'),
    # user app
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registration/', register_view, name='registration'),
    # course app
    path('courses/', course_list, name='course_list'),
    path('courses/<int:pk>/', course_details, name='course_details'),
    # user_course app
    path('user_courses/<int:pk>/', user_course_details, name='user_course_details'),
    path('courses/<int:pk>/purchase/', course_purchase, name='course_purchase'),
]
