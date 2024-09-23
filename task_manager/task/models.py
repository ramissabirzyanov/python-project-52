from django.db import models
from task_manager.user.models import User
from task_manager.status.models import Status
from task_manager.label.models import Label


class Task(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Имя')
    description = models.TextField(blank=True, verbose_name='Описание')
    status = models.ForeignKey(Status, related_name='status', on_delete=models.PROTECT, verbose_name='Статус')
    executor = models.ForeignKey(User, related_name='executor', null=True, blank=True, on_delete=models.PROTECT, verbose_name='Исполнитель')
    labels = models.ManyToManyField(Label, related_name='labels', blank=True, default='', verbose_name='Метки')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name='author', on_delete=models.PROTECT, verbose_name='Автор')

    class Meta:
        db_table = 'Task'
        verbose_name = 'Задача'

    def get_labels(self):
        return ",".join([str(label) for label in self.labels.all()])

    def __str__(self):
        return f"Задача {self.name} от {self.author}. Cтатус {self.status}. Исполняет {self.executor}"
