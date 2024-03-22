from django import forms

"""
This is a Login Form used to Authenticate users against the database
"""
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widgets=forms.PasswordInput) # Password Input Widget renders HTML password Element