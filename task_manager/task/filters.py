import django_filters
from task_manager.task.models import Task
from task_manager.status.models import Status
from task_manager.user.models import User
from task_manager.label.models import Label
from django import forms
from django.utils.translation import gettext_lazy as _


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(queryset=Status.objects.all())
    executor = django_filters.ModelChoiceFilter(queryset=User.objects.all())
    labels = django_filters.ModelChoiceFilter(queryset=Label.objects.all(),
                                              label=_('Label'))
    user_tasks = django_filters.BooleanFilter(widget=forms.CheckboxInput,
                                              field_name='author',
                                              method='filter_user_tasks',
                                              label=_("Only user's tasks"))

    def filter_user_tasks(self, queryset, name, value):
        if self.request.GET.get('user_tasks') is None:
            return queryset
        else:
            return queryset.filter(author=self.request.user)

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']
