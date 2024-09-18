from task_manager.task.models import Task
from task_manager.user.models import User
from task_manager.status.models import Status
from django import forms


class TaskCreateForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']


class TaskUpdateForm(TaskCreateForm):

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']


class TaskFilterForm(forms.ModelForm):
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=False, label='Статус')
    executor = forms.ModelChoiceField(queryset=User.objects.all(), required=False, label='Исполнитель')
    class Meta:
        model = Task
        fields = ['status', 'executor']
