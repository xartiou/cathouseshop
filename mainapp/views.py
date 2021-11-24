import os
from django.shortcuts import render

# Create your views here.
module_dir = os.path.dirname(__file__, )


def index(request):
    menu = {'title': 'Главная'}
    return render(request, "mainapp/index.html", menu)


links_menu = [
    {'url': 'products', 'title': 'все'},
    {'url': 'products_home', 'title': 'дом'},
    {'url': 'products_office', 'title': 'офис'},
    {'url': 'products_modern', 'title': 'модерн'},
    {'url': 'products_classic', 'title': 'классика'},
]


def products(request):
    context = {
        'links_menu': links_menu,
        'title': 'продукты'
    }
    return render(request, "mainapp/products.html", context)


def products_home(request):
    context = {
        'links_menu': links_menu,
        'title': 'дом'
    }
    return render(request, "mainapp/products.html", context)


def products_office(request):
    context = {
        'links_menu': links_menu,
        'title': 'офис'
    }
    return render(request, "mainapp/products.html", context)


def products_modern(request):
    context = {
        'links_menu': links_menu,
        'title': 'модерн'
    }
    return render(request, "mainapp/products.html", context)


def products_classic(request):
    context = {
        'links_menu': links_menu,
        'title': 'классика'
    }
    return render(request, "mainapp/products.html", context)


def contact(request):
    menu = {'title': 'контакты'}
    return render(request, "mainapp/contact.html", menu)
