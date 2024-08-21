from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    created_at = models.DateTimeField(auto_now=True,)
    
    class Meta:
        db_table = 'User'

    def __str__(self):
        return self.username

