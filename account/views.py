from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(
                username=data['username'],
                email=data['email'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                password=data['password1'],
            )
            messages.success(request, 'ثبت نام با موفقیت انجام شد', 'success')
            return redirect('home:mainpage')
    else:
        form = RegisterForm()
    context = {'form': form}
    return render(request, 'account/register.html', context)
    # return render(request, 'account:register', context)


def logins(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                user = authenticate(request, username=data['user'], password=data['password'])
            except:
                user = authenticate(request, username=User.objects.get(email=data['user']), password=data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'خوش اومدی!', 'success')
                return redirect('home:mainpage')
            else:
                messages.error(request, 'نام کابری یا رمز رو اشتباه وارد کردی', 'danger')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'account/login.html', context)


def logouts(request):
    logout(request)
    messages.success(request, 'خروج با موفقیت انجام شد', 'primary')
    return redirect('home:mainpage')


def dashboard(request):
    return render(request, 'account/dashboard.html')
