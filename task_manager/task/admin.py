from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'author',
        'status',
        'executor',
        'get_labels',
        'created_at',
        )
