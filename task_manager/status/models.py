from django.db import models
from django.utils.translation import gettext_lazy as _


class Status(models.Model):
    name = models.CharField(max_length=200,
                            unique=True,
                            verbose_name=_('Name'))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        db_table = 'Status'
        verbose_name = _('Status')

    def __str__(self):
        return self.name
