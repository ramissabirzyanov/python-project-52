from task_manager.task.models import Task
from django import forms
from task_manager.utils import UniqueNameErrorMixin

class TaskCreateForm(forms.ModelForm, UniqueNameErrorMixin):

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']


class TaskUpdateForm(TaskCreateForm, UniqueNameErrorMixin):

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
