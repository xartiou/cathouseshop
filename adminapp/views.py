from authapp.models import ShopUser
from django.shortcuts import get_object_or_404, render
from mainapp.models import Product, ProductCategory

# user


def user_create(request):
    context = {

    }
    return render(request, '', context=context)


def users(request):
    context = {
        'title': 'админка/пользователи',
        'object_list': ShopUser.objects.all().order_by('-is_active')
    }
    return render(request, 'adminapp/users.html', context=context)


def user_update(request):
    context = {

    }
    return render(request, '', context=context)


def user_delete(request):
    context = {

    }
    return render(request, '', context=context)

# category


def category_create(request):
    context = {

    }
    return render(request, '', context=context)


def categories(request):
    context = {
        'title': 'админка/категории',
        'object_list': ProductCategory.objects.all().order_by('-is_active')
    }
    return render(request, 'adminapp/categories.html', context=context)


def category_update(request):
    context = {

    }
    return render(request, '', context=context)


def category_delete(request):
    context = {

    }
    return render(request, '', context=context)

# product


def product_create(request):
    context = {

    }
    return render(request, '', context=context)


def products(request, pk):
    context = {
        'category': get_object_or_404(ProductCategory, pk=pk),
        'object_list': Product.objects.filter(category__pk=pk).order_by('-is_active')
    }
    return render(request, 'adminapp/products.html', context=context)


def product_update(request):
    context = {

    }
    return render(request, '', context=context)


def product_delete(request):
    context = {

    }
    return render(request, '', context=context)


def product_detail(request):
    context = {

    }
    return render(request, '', context=context)