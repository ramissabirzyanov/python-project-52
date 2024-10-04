from task_manager.task.models import Task
from task_manager.forms import CommonInfoForm


class TaskCreateForm(CommonInfoForm):

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']


class TaskUpdateForm(CommonInfoForm):

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
