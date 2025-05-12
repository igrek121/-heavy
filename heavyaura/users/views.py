from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import UserLoginForm

def login(request):
    if request.methot == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,
                                     password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:priduct'))
        else:
            form = UserLoginForm()

    return render(request, 'users/login.html', {'form': form})


def regisration(request):
    return render(request, 'users/register.html')


def profile(request):
    return render(request, 'users/profile.html')


def logout(request):
    ...