from django.db import models
from task_manager.user.models import User
from task_manager.status.models import Status
from task_manager.label.models import Label
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    name = models.CharField(max_length=200,
                            unique=True,
                            verbose_name=_('Name'))
    description = models.TextField(blank=True, verbose_name=_('Discription'))
    status = models.ForeignKey(
        Status,
        related_name='status',
        on_delete=models.PROTECT,
        verbose_name=_('Status'))
    executor = models.ForeignKey(
        User,
        related_name='executor',
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        verbose_name=_('Executor'))
    labels = models.ManyToManyField(
        Label,
        through='TaskLabels',
        related_name='labels',
        blank=True,
        verbose_name=_('Labels'))
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        related_name='author',
        on_delete=models.PROTECT,
        verbose_name=_('Author'))

    class Meta:
        db_table = 'Task'
        verbose_name = _('Task')

    def get_labels(self):
        return ",".join([str(label) for label in self.labels.all()])

    def __str__(self):
        return self.name


class TaskLabels(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    labels = models.ForeignKey(Label, on_delete=models.PROTECT)
