from django.db import models


class PostCategory(models.Model):
    title = models.CharField(max_length=511)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"
