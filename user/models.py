from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    achievements = models.ManyToManyField(
        'course.Achievement',
        related_name='users',
        help_text='Achievements of the user',
        through='user_course.UserAchievement',
    )
