from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Имя')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Status'
    
    def __str__(self):
        return self.name
