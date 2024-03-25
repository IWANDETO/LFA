from django import forms

"""
This is a Login Form used to Authenticate users against the database
"""
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput) # Password Input Widget renders HTML password Element