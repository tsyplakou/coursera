from django.db import models
from django.core.validators import MaxValueValidator


class UserCourse(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.PROTECT)
    course = models.ForeignKey('course.Course', on_delete=models.PROTECT)
    join_date = models.DateTimeField(auto_now_add=True)
    progress = models.PositiveIntegerField(
        default=0,
        validators=[MaxValueValidator(100)],
    )
