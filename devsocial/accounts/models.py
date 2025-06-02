from django.db import models
from django.contrib.auth.models import AbstractUser 


class CustomUserRole(models.Model):
    role = models.CharField(max_length=50)
    description = models.CharField(max_length=255 , null=True , blank=True)

    def __str__(self):
        return self.role
    

class CustomUser(AbstractUser):
    role = models.ForeignKey(CustomUserRole, on_delete=models.SET_NULL, null=True , blank = True)

    def can_delete_posts(self):
        return self.role and self.role.name in ['superuser', 'moderator']

    def can_create_posts(self):
        return self.role and self.role.name in ['superuser', 'moderator', 'user']
