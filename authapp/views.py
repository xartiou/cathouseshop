from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from authapp.forms import ShopUserLoginForm


def login(request):
    login_form = ShopUserLoginForm(data=request.POST)
    if request.metod == 'POST' and login_form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))
    context = {
        'login_form':login_form
    }


        return render(request, '', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
