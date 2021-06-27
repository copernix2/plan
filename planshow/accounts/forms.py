from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput

class PasswordChangingForm(PasswordChangeForm) :
    old_password= forms.CharField(widget=PasswordInput(attrs={'class': 'form-control', 'type': 'password'}), label='Ancien mot de passe')
    new_password1=forms.CharField(widget=PasswordInput(attrs={'class': 'form-control'}), label='Nouveau mot de passe')
    new_password2=forms.CharField(widget=PasswordInput(attrs={'class': 'form-control'}), label='Confirmez le mot de passe')
    class meta:
        model= User
        fields=('old_password', 'new_password1', 'new_password2')
        

