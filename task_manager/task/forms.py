from task_manager.task.models import Task
from task_manager.utils import CommonInfoForm


class TaskCreateForm(CommonInfoForm):

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']


class TaskUpdateForm(CommonInfoForm):

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
