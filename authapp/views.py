from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from django.shortcuts import render


# Create your views here.

def login(request):
    pass


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
