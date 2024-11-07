from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'price',
        'duration',
        'discounted_price',
        'discounted_price_twice',
    )
    search_fields = ('title', 'description', 'price', 'duration')
    list_editable = ('duration',)
    ordering = ('title',)
    list_filter = ('price', 'duration')

    actions = ['increase_price_by_10', 'decrease_price_by_10']

    def increase_price_by_10(self, request, queryset):
        for obj in queryset:
            obj.price += 10
            obj.save()
    increase_price_by_10.short_description = 'Увеличить цену на 10'

    def decrease_price_by_10(self, request, queryset):
        for obj in queryset:
            obj.price -= 10
            obj.save()
    decrease_price_by_10.short_description = 'Уменшить цену на 10'

    def discounted_price_twice(self, obj):
        return ((obj.price / 2), (obj.price / 2))
    discounted_price_twice.short_description = _('Discounted Twice')

    # fields = (('title', 'description'), 'price', 'duration')
    fieldsets = (
        (_('Course info'), {
            'fields': ('title', 'description'),
        }),
        (_('Course Details'), {
            'fields': ('price', 'duration'),
        }),
    )
