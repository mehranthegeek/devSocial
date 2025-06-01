from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserRegistrationForm, CustomUserLoginForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog:homepage')  
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('blog:homepage')  
    else:
        form = CustomUserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')



def logout_view(request):
    logout(request)
    return redirect('blog:homepage')