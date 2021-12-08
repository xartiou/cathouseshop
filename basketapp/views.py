from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product


def basket(request):
    pass


def add(request, pk):
    product_item = get_object_or_404(Product, pk=pk)

    basket_item = Basket.objects.filter(product=product_item, user=request.user).first()

    if not basket_item:
        basket_item = Basket(product=product_item, user=request.user)

    basket_item.quantity += 1
    basket_item.save()

    # возвращаем пользователя на  ту страницу где он был используя метаданные
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove(request, pk):
    basket_item = get_object_or_404(Basket, pk=pk)
    basket_item.delete()
    # возвращаем пользователя на  ту страницу где он был используя метаданные
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
