from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import LoginForm

"""
Instantiate a new login form when user_login view is called with a GET request
"""
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST) # Instantiate form
        if form.is_valid(): # Check if form is valid
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'] ) #Authenticate User if form is valid
            if user is not None:
                if user.is_active:
                    login(request, user) # Login user if active
                    return HttpResponse('User Authenticated Successfully') 
                else:
                    return HttpResponse('User Account Disabled!') # Return Response is user is not active
            else:
                return HttpResponse('Invalid Login') # Return Response if user is not authenticated
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})
        

            




# Create your views here.