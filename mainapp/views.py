import json
import os
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from basketapp.models import Basket
from mainapp.models import Product, ProductCategory


# Create your views here.
module_dir = os.path.dirname(__file__, )


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def index(request):
    context = {
        'products': Product.objects.all()[2:5],
        'title': 'главная',
        'basket': get_basket(request.user)
    }
    return render(request, "mainapp/index.html", context=context)


def get_hot_product():
    return random.sample(list(Product.objects.all()), 1)[0]


def get_same_products(hot_product):
    products_list = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    return products_list


def products(request, pk=None, page=1):
    links_menu = ProductCategory.objects.all()
    products = Product.objects.filter(is_active=True, category__is_active=True)
    # file_path = os.path.join(module_dir, 'fixtures/products.json')
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

        paginator = Paginator(products_list, 2)  # передаем откуда и сколько выводить
        try:
            products_paginator = paginator.page(page)  # с какой страницы по умолчанию
        except PageNotAnInteger:  # обрабатываем исключение нецифрового номера страницы
            products_paginator = paginator.page(1)  # выводим первую страницу
        except EmptyPage:  # обрабатываем исключение превышенного номера страницы
            products_paginator = paginator.page(paginator.num_pages)  # выводим последнюю страницу

        context = {
            'links_menu': links_menu,
            'title': 'продукты',
            'category': category_item,
            'products': products_paginator,
            'basket': get_basket(request.user)
        }
        return render(request, "mainapp/products_list.html", context=context)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    context = {
        'links_menu': links_menu,
        'title': 'продукты',
        'products': products,
        'hot_product': hot_product,
        'same_products': same_products,
        'basket': get_basket(request.user)
    }
    return render(request, 'mainapp/products.html', context=context)


def product(request, pk):
    context = {
        'title': 'продукты',
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),

    }
    return render(request, 'mainapp/product.html', context=context)


def contact(request):
    context = {
        'title': 'контакты',
        'basket': get_basket(request.user)
    }
    return render(request, "mainapp/contact.html", context=context)
