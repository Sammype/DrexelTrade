from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

def ensure_endswith(input):
    for number in range(1):
        if input.endswith('@drexel.edu'):
            break
        else:
            input = forms.EmailField()
            print('You must use an email that ends with @drexel.edu')
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    ensure_endswith(email)
        

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
