from django.contrib import admin
from .models import CustomUserRole,CustomUser

admin.site.register(CustomUserRole)
admin.site.register(CustomUser)
