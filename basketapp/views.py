from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.urls import reverse
from basketapp.models import Basket
from mainapp.models import Product


@login_required
def basket(request):  # отображение корзины
    title = 'корзина'
    basket_list = Basket.objects.filter(user=request.user)  # выбираем все корзины текущего авторизованного пользователя

    context = {
        'baskets': basket_list,
        'title': title
    }
    return render(request, 'basketapp/basket.html', context)


@login_required
def add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('products:product', args=[pk]))

    product_item = get_object_or_404(Product, pk=pk)
    basket_item = Basket.objects.filter(product=product_item, user=request.user).first()

    if not basket_item:
        basket_item = Basket(product=product_item, user=request.user)

    basket_item.quantity += 1
    basket_item.save()

    # возвращаем пользователя на  ту страницу где он был используя метаданные
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def remove(request, pk):
    basket_item = get_object_or_404(Basket, pk=pk)
    basket_item.delete()
    # возвращаем пользователя на  ту страницу где он был используя метаданные
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def edit(request, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        new_basket_item = Basket.objects.get(pk=int('pk'))

        if quantity > 0:
            new_basket_item.quantity = quantity
            new_basket_item.save()
        else:
            new_basket_item.delete()

        basket_item = Basket.objects.filter(user=request.user).order_by('product')

        context = {
            'basket_items': basket_item
        }

        result = render_to_string('basketapp/includes/inc_baskets_list.html', context)

        return JsonResponse({'result': result})


