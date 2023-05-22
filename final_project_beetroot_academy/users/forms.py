from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class RegistrationUserForm(UserCreationForm):
    email = forms.EmailField()
    # add more fields for profile

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class ChangeUserDataForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ChangeProfileDataForm(forms.ModelForm):


    class Meta:
        model = Profile
        fields = ['birthday','country','about','img']
