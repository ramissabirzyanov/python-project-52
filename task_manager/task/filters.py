import django_filters
from task_manager.task.models import Task
from task_manager.status.models import Status
from task_manager.user.models import User
from django import forms


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(queryset=Status.objects.all())
    executor = django_filters.ModelChoiceFilter(queryset=User.objects.all())
    user_tasks = django_filters.BooleanFilter(widget=forms.CheckboxInput,
                                              field_name='author',
                                              method='filter_user_tasks',
                                              label=('Только свои задачи'))

    def filter_user_tasks(self, queryset, name, value):
        if self.request is None:
            return queryset
        else:
            return queryset.filter(value)

    class Meta:
        model = Task
        fields = ['status', 'executor']
