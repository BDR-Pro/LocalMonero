from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import re
from user.models import Profile
from django.contrib.auth.decorators import login_required

def login(request):
    """
    login view

    Args:
        request 

    Returns:
        render: render login.html
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('user:profile')
        else:
            return render(request, 'user/login.html', {'error': 'Invalid username or password'})
    return render(request, 'user/login.html')

def register(request):
    """
    register view

    Args:
        request 

    Returns:
        render: render register.html
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        email = request.POST['email']

        # Email regex pattern
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_pattern, email):
            return render(request, 'user/register.html', {'error': 'Invalid email format'})

        # Password regex pattern (at least 8 characters, one uppercase, one lowercase, one number)
        password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$'
        if not re.match(password_pattern, password):
            return render(request, 'user/register.html', {'error': 'Password must be at least 8 characters long and include one uppercase letter, one lowercase letter, and one number'})

        if password == password_confirm:
            try:
                # Validate email using Django's validate_email method
                validate_email(email)
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                return redirect('user:login')
            except ValidationError:
                return render(request, 'user/register.html', {'error': 'Invalid email'})
            except:
                return render(request, 'user/register.html', {'error': 'Username already exists'})
        else:
            return render(request, 'user/register.html', {'error': 'Passwords do not match'})
    return render(request, 'user/register.html')

@login_required(login_url='user:login')
def logout(request):
    """
    logout view

    Args:
        request 

    Returns:
        redirect: redirect to login
    """
    auth_logout(request)
    return redirect('user:login')

@login_required(login_url='user:login')
def profile(request):
    """
    profile view

    Args:
        request 

    Returns:
        render: render profile.html
    """
    #get or create profile
    profile = Profile.objects.get_or_create(user=request.user)[0]
    return render(request, 'user/profile.html', {'profile': profile})


@login_required(login_url='user:login')
def calculate_xmr_balance(request):
    profile = Profile.objects.get(user=request.user)
    profile.calculate_xmr_balance()
    return redirect('user:profile')

@login_required(login_url='user:login')
def calculate_btc_balance(request):
    profile = Profile.objects.get(user=request.user)
    profile.calculate_btc_balance()
    return redirect('user:profile')