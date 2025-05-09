from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def TestPage(request):
    testObjects = Post.objects.all()
    return render(request, 'blog/testPage.html', {'testObjects':testObjects} )

def user_dashboard(request):
    return HttpResponse(f"{request.user.username} - {request.user.email} - {request.user.password}")