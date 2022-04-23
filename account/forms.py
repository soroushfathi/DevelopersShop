from django import forms
from django.contrib.auth.models import User
from .models import Profile
import re

errors = {
    'min_lenght': 'حداکثر طول را رعایت کنید',
    'max_lenght': 'حداقل طول',
    'required': 'این فیلد باید پر شود',
}


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=25, min_length=5, error_messages=errors)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': ''}))
    first_name = forms.CharField(min_length=3, max_length=30)
    last_name = forms.CharField(min_length=3, max_length=30)
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'رمز'}))
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'تکرار رمز'}))

    def clean_username(self):
        un = self.cleaned_data['username']
        if User.objects.filter(username=un).exists():
            raise forms.ValidationError('این نام کاربری قبلا استفاده شده است')

        return un

    def clean_email(self):
        e = self.cleaned_data['email']
        if User.objects.filter(email=e).exists():
            raise forms.ValidationError('این ایمیل قبلا استفاده شده است')

        return e

    def clean_password2(self):
        p1 = self.cleaned_data['password1']
        p2 = self.cleaned_data['password2']
        pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
        if p1 != p2:
            raise forms.ValidationError('رمز تکرار شده اشتباه نوشته شده است')
        if not re.findall(pattern, p1):
            raise forms.ValidationError('رمز باید حداقل شامل یک عدد. حرف بزرگ و کوچک و ۸ کارکتر باشد')
        return p1


class LoginForm(forms.Form):
    user = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'enter username or email'}))
    password = forms.CharField(widget=forms.PasswordInput)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'address']
