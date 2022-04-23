from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Profile
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data['username'],
                email=data['email'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                password=data['password1'],
            )
            user.save()
            messages.success(request, 'ثبت نام با موفقیت انجام شد', 'success')
            logins(request)
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


@login_required(login_url='account:login')
def dashboard(request):
    profile = Profile.objects.get(user_id=request.user.id)
    context = {'profile': profile, }
    return render(request, 'account/dashboard.html', context=context)


@login_required(login_url='account:login')
def user_update(requset):
    if requset.method == 'POST':
        user_form = UserUpdateForm(requset.POST, instance=requset.user)
        profile_form = ProfileUpdateForm(requset.POST, instance=requset.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(requset, 'تغییرات با موفقیت انجام شد', 'success')
            return redirect('account:dashboard')
    else:
        user_form = UserUpdateForm(instance=requset.user)
        profile_form = ProfileUpdateForm(instance=requset.user.profile)
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(requset, 'account/update.html', context=context)


@login_required(login_url='account:login')
def change_passsword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'تغییر رمز با موفقیت انجام شد', 'success')
            return redirect('account:dashboard')
        else:
            messages.error(request, 'رمز وارد شده اشتباه است', 'danger')
            return redirect('account:change-password')

    else:
        form = PasswordChangeForm(request.user)
        context = {
            'form': form,
        }
        return render(request, 'account/change-password.html', context=context)
