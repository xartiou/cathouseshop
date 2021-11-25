import json
import os
from django.shortcuts import render
from mainapp.models import Product, ProductCategory

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
    context = {
        'products': Product.objects.all()[:4],
        'title': 'главная'}
    return render(request, "mainapp/index.html", context)


def products(request, pk=None):
    file_path = os.path.join(module_dir, 'fixtures/products.json')
    products = json.load(open(file_path, encoding='utf-8'))
    context = {
        'links_menu': ProductCategory.objects.all(),
        'title': 'продукты',
        'products': products,

    }
    return render(request, "mainapp/products.html", context)


def contact(request):
    context = {'title': 'контакты'}
    return render(request, "mainapp/contact.html", context)
