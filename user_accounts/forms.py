from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegister(forms.Form):
    usable_password = None

    class Meta:
        model = User
        fields = ['f_name', 'l_name', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(UserRegister, self).__init__(*args, **kwargs)
        self.fields['f_name'] = forms.CharField(label='First Name', max_length=100, required=True,
                                                widget=forms.TextInput(attrs={'class': 'form-control'}))
        self.fields['l_name'] = forms.CharField(label='Last Name', max_length=100, required=True,
                                                widget=forms.TextInput(attrs={'class': 'form-control'}))
        self.fields['email'] = forms.EmailField(label='Email', max_length=100, required=True,
                                                widget=forms.EmailInput(attrs={'class': 'form-control'}))
        self.fields['password'] = forms.CharField(label='Password', max_length=100,
                                                  widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                                  required=True)
