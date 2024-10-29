from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    courses = models.ManyToManyField(
        'course.Course',
        related_name='users',
        help_text='Courses taken by the user',
        through='user_course.UserCourse',
    )
    achievements = models.ManyToManyField(
        'course.Achievement',
        related_name='users',
        help_text='Achievements of the user',
        through='user_course.UserAchievement',
    )
    balance = models.DecimalField(decimal_places=2, max_digits=10, default=0)
