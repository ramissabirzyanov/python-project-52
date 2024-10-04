from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'User'
        ordering = ['id']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
