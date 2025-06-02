from django.db import models
from django.contrib.auth.models import User
from accounts.models import CustomUser

class PostCategory(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

class Post(models.Model):
    title = models.CharField(max_length=255)  
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    content = models.TextField() 
    category = models.ForeignKey(
        PostCategory, on_delete=models.CASCADE, related_name='posts'
    )
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='posts'
    ) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.title


    
