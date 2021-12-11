from authapp.forms import ShopUserRegisterForm
from adminapp.forms import ShopUserAdminEditForm
from authapp.models import ShopUser
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from mainapp.models import Product, ProductCategory
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse

# user


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):

    title = 'пользователи/создание'

    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)

        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('adminapp:user_list'))
    else:
        user_form = ShopUserRegisterForm()

    context = {
        'title': title,
        'form': user_form
    }
    return render(request, 'adminapp/user_form.html', context=context)


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    context = {
        'title': 'админка/пользователи',
        'object_list': ShopUser.objects.all().order_by('-is_active')
    }
    return render(request, 'adminapp/users.html', context=context)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    title = 'пользователи/редактирование'

    edit_user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        user_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)

        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('adminapp:user_list'))
    else:
        user_form = ShopUserAdminEditForm(instance=edit_user)

    context = {
        'title': title,
        'form': user_form
    }
    return render(request, 'adminapp/user_form.html', context=context)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    title = 'пользователи/удаление'

    edit_user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        if edit_user.is_active:
            edit_user.is_active = False  # деактивируем пользователя
        else:
            edit_user.is_active = True
        edit_user.save()
        return HttpResponseRedirect(reverse('adminapp:user_list'))
    context = {
        'title': title,
        'object': edit_user
    }
    return render(request, 'user_delete.html', context=context)

# category


@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    context = {

    }
    return render(request, '', context=context)


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    context = {
        'title': 'админка/категории',
        'object_list': ProductCategory.objects.all().order_by('-is_active')
    }
    return render(request, 'adminapp/categories.html', context=context)


@user_passes_test(lambda u: u.is_superuser)
def category_update(request):
    context = {

    }
    return render(request, '', context=context)


@user_passes_test(lambda u: u.is_superuser)
def category_delete(request):
    context = {

    }
    return render(request, '', context=context)

# product


@user_passes_test(lambda u: u.is_superuser)
def product_create(request):
    context = {

    }
    return render(request, '', context=context)


@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    context = {
        'category': get_object_or_404(ProductCategory, pk=pk),
        'object_list': Product.objects.filter(category__pk=pk).order_by('-is_active')
    }
    return render(request, 'adminapp/products.html', context=context)


@user_passes_test(lambda u: u.is_superuser)
def product_update(request):
    context = {

    }
    return render(request, '', context=context)


@user_passes_test(lambda u: u.is_superuser)
def product_delete(request):
    context = {

    }
    return render(request, '', context=context)


@user_passes_test(lambda u: u.is_superuser)
def product_detail(request):
    context = {

    }
    return render(request, '', context=context)
