import json
import os
import random

from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory

# Create your views here.
module_dir = os.path.dirname(__file__, )


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    return []


def index(request):
    context = {
        'products': Product.objects.all()[2:5],
        'title': 'главная',
        'basket': get_basket(request.user)
    }
    return render(request, "mainapp/index.html", context=context)


def products(request, pk=None):
    links_menu = ProductCategory.objects.all()

    file_path = os.path.join(module_dir, 'fixtures/products.json')
    # products = json.load(open(file_path, encoding='utf-8'))

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
            'basket': get_basket(request.user)
        }
        return render(request, "mainapp/products_list.html", context=context)

    hot_product = random.sample(list(Product.objects.all()), 1)[0]
    same_products = Product.objects.all()[3:6]
    context = {
        'links_menu': links_menu,
        'title': 'продукты',
        'products': products,
        'hot_product': hot_product,
        'same_products': same_products,
        'basket': get_basket(request.user)
    }
    return render(request, "mainapp/products.html", context=context)


def contact(request):
    context = {
        'title': 'контакты',
        'basket': get_basket(request.user)
    }
    return render(request, "mainapp/contact.html", context)
