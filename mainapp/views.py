import json
import os
from django.shortcuts import render

# Create your views here.
module_dir = os.path.dirname(__file__,)

links_menu = [
    {'url': 'products', 'title': 'все'},
    {'url': 'products_home', 'title': 'дом'},
    {'url': 'products_office', 'title': 'офис'},
    {'url': 'products_modern', 'title': 'модерн'},
    {'url': 'products_classic', 'title': 'классика'},
]


menu = [
    {'href': 'index', 'title': 'главная'},
    {'href': 'products', 'title': 'продукты'},
    {'href': 'contact', 'title': 'контакты'},

]


def index(request):
    context = {'title': 'главная'}
    return render(request, "mainapp/index.html", context)


def products(request):
    file_path = os.path.join(module_dir, 'fixtures/products.json')
    products = json.load(open(file_path, encoding='utf-8'))
    context = {
        'links_menu': links_menu,
        'title': 'продукты',
        'products': products,

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
    context = {'title': 'контакты'}
    return render(request, "mainapp/contact.html", context)
