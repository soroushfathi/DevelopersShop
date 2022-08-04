from django.forms import ModelForm
from .models import Order
from django import forms

errors = {
    'min_lenght': 'حداکثر طول را رعایت کنید',
    'max_lenght': 'حداقل طول',
    'required': 'این فیلد باید پر شود',
}


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'postal_code', 'email', 'address']
        error_messages = errors

    def clean_postal_code(self):
        pc = self.cleaned_data['postal_code']
        if pc is not None:
            flags = [len(pc) != 10, '0' in pc, '2' in pc]
            if any(flags):
                raise forms.ValidationError('کد پستی معتبر نیست')
        else:
            raise forms.ValidationError('کدپستی نباید خالی نباشد')
        return pc

    def clean_address(self):
        address = self.cleaned_data['address']
        if address is None:
            raise forms.ValidationError('کدپستی نباید خالی نباشد')
        return address
