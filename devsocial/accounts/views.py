from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

@login_required
def user_dashboard(request):
    user = request.user
    return HttpResponse(f"سلام {user.username} عزیز! خوش آمدی 🌟")