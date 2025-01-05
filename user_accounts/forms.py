from django import forms

class UserRegister(forms.Form):
    file = forms.FileField()