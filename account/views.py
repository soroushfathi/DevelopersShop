from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.views import View
from django.utils.encoding import force_str, force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from six import text_type


class EmailTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return text_type(user.profile.is_email_active) + text_type(user.id) + text_type(timestamp)


etg = EmailTokenGenerator()


def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data['username'],
                email=data['email'],
                first_name=data['first_name'],
                # last_name=data['last_name'],
                password=data['password1'],
            )
            user.save()
            domain = get_current_site(request).domain
            uidb64 = urlsafe_base64_encode(force_bytes(user.id))
            url = reverse('account:email-activation', kwargs={'uidb64': uidb64, 'token': etg.make_token(user)})
            link = 'http://' + domain + url
            etext = '''
                سلام {} عزیز، به سایت فروشگاه برنامه نویسان خوش اومدی، برای فعال شدن حسابت
                روی لینک زیر کلیک کن(مدت اعتبار لینک 3 روز میباشد):\n
                {}
            '''.format(f'{user.first_name} {user.last_name}', link)
            email = EmailMessage(
                'activation email', etext, 'test<soroush8fathi@gmail.com>', [data['email']],
            )
            email.send(fail_silently=False)
            messages.success(request,
                             'ثبت نام با موفقیت انجام شد، برای فعال سازی حساب به ایمیل خود مراجعه کنید.', 'success')
            logins(request)
            return redirect('home:mainpage')
        else:
            return render(request, 'account/register.html', {'form': form})
    return render(request, 'account/register.html', {'form': form})


class EmailRegister(View):
    def get(self, request, uidb64, token):
        uid = force_str(urlsafe_base64_decode(uidb64))
        try:
            user = User.objects.get(id=uid)
            if user and etg.check_token(user, token):
                user.profile.is_email_active = True
                user.profile.save()
                user.save()
                messages.error(request, 'ایمیل با موفقیت تایید شد', 'error')
                return redirect('account:dashboard')
        except User.DoesNotExist:
            messages.error(request, 'همچین کاربری یافت نشد', 'error')
            return redirect('account:dashboard')


@login_required(login_url='account:login')
def resend_email_activation(request):
    user = request.user
    domain = get_current_site(request).domain
    uidb64 = urlsafe_base64_encode(force_bytes(user.id))
    url = reverse('account:email-activation', kwargs={'uidb64': uidb64, 'token': etg.make_token(user)})
    link = 'http://' + domain + url
    etext = '''
                    سلام {} عزیز، به سایت فروشگاه برنامه نویسان خوش اومدی، برای فعال شدن حسابت
                    روی لینک زیر کلیک کن(مدت اعتبار لینک 3 روز میباشد):\n
                    {}
                '''.format(f'{user.first_name} {user.last_name}', link)
    email = EmailMessage(
        'activation email', etext, 'test<soroush8fathi@gmail.com>', [request.user.email],
    )
    email.send(fail_silently=False)
    messages.success(request, 'ایمیل تایید حساب مجددا فرستاده شد.', 'success')
    return redirect('account:dashboard')


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
                return redirect('account:login')
        return render(request, 'account/login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})


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
            # todo: check update email
            # if requset.user.email != profile_form.cleaned_data['email']:
            #     requset.user.profile.is_email_active = False
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


class ResetPassword(auth_views.PasswordResetView):
    """
        get email, create link and send it for reset password
    """
    template_name = 'account/reset-password.html'
    success_url = reverse_lazy('account:done-reset-password')
    email_template_name = 'account/link.html'


# todo debug reset password
class DoneResetPassword(auth_views.PasswordResetDoneView):
    """
        show sending proccess was seccussful
    """
    template_name = 'account/done-reset-password.html'


class ConfirmResetPassword(auth_views.PasswordResetConfirmView):
    """
        submit new password, redirect it to complete level
    """
    template_name = 'account/confirm-reset-password.html'
    success_url = reverse_lazy('account:complete-reset-password')


class CompleteResetPassword(auth_views.PasswordResetCompleteView):
    template_name = 'account/complete-reset-password.html'
