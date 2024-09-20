from django.db import models


class Label(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Имя')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Label'

    def __str__(self):
        return self.name
