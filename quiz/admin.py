from django.contrib import admin

from .models import Quiz, Question, Choice


class QuestionInline(admin.TabularInline):  # или admin.StackedInline
    model = Quiz.questions.through
    extra = 0


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


class ChoiceInline(admin.TabularInline):  # или admin.StackedInline
    model = Choice
    extra = 0


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ( 'text', )
    inlines = [ChoiceInline]
