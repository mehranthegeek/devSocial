from django.db import models

class Test(models.Model):
    title = models.CharField(max_length=100)
    

class PostCategory(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

