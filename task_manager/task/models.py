from django.db import models
from task_manager.user.models import User
from task_manager.status.models import Status


class Task(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    status = models.ForeignKey(Status, related_name='status', on_delete=models.PROTECT)
    executor = models.ForeignKey(User, related_name='executor', null=True, blank=True, on_delete=models.PROTECT)
    label = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name='author', on_delete=models.PROTECT)

    class Meta:
        db_table = 'Task'

    def __str__(self):
        return f"Задача {self.name} от {self.author}. Cтатус {self.status}. Исполняет {self.executor}"
