from django.forms import ModelForm
from .models import AddContact
from django import forms


class AddContactForm(ModelForm):
    class Meta:
        model = AddContact
        fields = ['name', 'company', 'mobile']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'})
                   }



