from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=250)
    questions = models.ManyToManyField('Question', related_name='quizzes')

    def __str__(self):
        return self.title


class Question(models.Model):
    # quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=250)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
