from django import forms
from .models import ContactUs

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields=['name', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                   'placeholder': 'نام',}),
            'phone': forms.TextInput(attrs={'class': 'form-control',
                    'placeholder': 'شماره تماس',}),
            'message': forms.Textarea(attrs={'class': 'form-control',
                     'placeholder': 'پیام',}),
        }