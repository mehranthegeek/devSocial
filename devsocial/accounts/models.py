from django.db import models

class CustomUserRole(models.Model):
    role = models.CharField(max_length=50)
    description = models.CharField(max_length=255 , null=True , blank=True)

    def __str__(self):
        return self.role
