from django.urls import path
from .views import homepage, add_post, profile, update_post, delete_post, post_detail, category_posts

app_name = 'blog'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('add/', add_post, name='add_post'),
    path('profile/', profile, name='profile'),
    path('post/<int:post_id>/edit/', update_post, name='update_post'),
    path('post/<int:post_id>/delete/', delete_post, name='delete_post'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('category/<int:category_id>/', category_posts, name='category_posts'),
]
