from django.core.validators import MinValueValidator
from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=80, help_text='Course title')
    description = models.TextField(help_text='Course description')

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='Course price',
        validators=[MinValueValidator(0),]
    )
    duration = models.PositiveSmallIntegerField(
        help_text='Course duration in weeks',
    )

    def __str__(self):
        return self.title


class Achievement(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.PROTECT,
        related_name='achievements',
        help_text='Course associated with the achievement',
    )
    name = models.CharField(max_length=50, help_text='Achievement name')
    description = models.TextField(help_text='Achievement description')
    score = models.PositiveSmallIntegerField(help_text='Achievement score')
