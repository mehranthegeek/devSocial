from django.urls import path
from . import views 
from .views import profile

urlpatterns = [
    path('test/',views.TestPage , name='test'),
    path('profile/', profile, name='profile'),
]
