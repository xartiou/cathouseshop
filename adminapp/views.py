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
        'object_list': Product.objects.all().order_by('-is_active')
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
        'object_list': ShopUser.objects.filter(category__pk=pk).order_by('-is_active')
    }
    return render(request, 'mainapp/products.html', context=context)


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
