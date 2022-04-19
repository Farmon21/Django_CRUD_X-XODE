from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':"input"})),
    label = ('Create Any Username')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}), label='Enter Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}), label='Repeat Password')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label='Enter Your Username')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}), label='Enter Password')

    class Meta:
        model = User
        fields = ['username', 'password']

