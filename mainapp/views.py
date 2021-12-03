import json
import os
from django.shortcuts import render, get_object_or_404
from mainapp.models import Product, ProductCategory

# Create your views here.
module_dir = os.path.dirname(__file__, )

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
    return render(request, "mainapp/index.html", context=context)


def products(request, pk=None):
    links_menu = ProductCategory.objects.all()

    file_path = os.path.join(module_dir, 'fixtures/products.json')
    products = json.load(open(file_path, encoding='utf-8'))

    if pk is not None:
        if pk == 0:
            products_list = Product.objects.all()
            category_item = {
                'name': 'все',
                'pk': 0
            }
        else:
            category_item = get_object_or_404(ProductCategory, pk=pk)
            products_list = Product.objects.filter(category__pk=pk)
        context = {
            'links_menu': links_menu,
            'title': 'продукты',
            'category': category_item,
            'products': products_list,
        }
        return render(request, "mainapp/products_list.html", context=context)

    context = {
        'links_menu': links_menu,
        'title': 'продукты',
        'products': products,

    }
    return render(request, "mainapp/products.html", context=context)


def contact(request):
    context = {'title': 'контакты'}
    return render(request, "mainapp/contact.html", context)
