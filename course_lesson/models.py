from django.db import models


class Lesson(models.Model):
    """a.k.a. lesson"""
    is_free = models.BooleanField(default=False, help_text='Is lesson free?')
    ordering_number = models.PositiveSmallIntegerField(
        help_text='Lesson ordering number in course',
    )
    course = models.ForeignKey(
        'course.Course',
        on_delete=models.PROTECT,
        related_name='contents',
        help_text='Course associated with the content',
    )
    title = models.CharField(max_length=80, help_text='Content title')


class Content(models.Model):
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.PROTECT,
        related_name='contents',
        help_text='Lesson associated with the quiz',
    )
    text = models.TextField(help_text='Content text')
    document = models.FileField(upload_to='documents/', help_text='Content document')
