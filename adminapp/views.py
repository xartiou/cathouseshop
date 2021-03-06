from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from authapp.forms import ShopUserRegisterForm
from adminapp.forms import ShopUserAdminEditForm, ProductCategoryEditForm, ProductEditForm
from authapp.models import ShopUser
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from mainapp.models import Product, ProductCategory
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class AccessMixin:  # проверка на  is_superuser

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

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


# @user_passes_test(lambda u: u.is_superuser)
# def users(request):
#     context = {
#         'title': 'админка/пользователи',
#         'object_list': ShopUser.objects.all().order_by('-is_active')
#     }
#     return render(request, 'adminapp/users.html', context=context)

class UsersListView(ListView, AccessMixin):
    model = ShopUser  # название класса модели
    template_name = 'adminapp/users.html'  # путь к шаблону


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


# @user_passes_test(lambda u: u.is_superuser)
# def category_create(request):
#     title = 'категории/создание'
#
#     if request.method == 'POST':
#         category_form = ProductCategoryEditForm(request.POST, request.FILES)
#
#         if category_form.is_valid():
#             category_form.save()
#             return HttpResponseRedirect(reverse('adminapp:categories'))
#     else:
#         category_form = ProductCategoryEditForm()
#
#     context = {
#         'title': title,
#         'form': category_form
#     }
#     return render(request, 'adminapp/category_create.html', context=context)

class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_create.html'
    success_url = reverse_lazy('adminapp:categories')
    fields = '__all__'


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    context = {
        'title': 'админка/категории',
        'object_list': ProductCategory.objects.all().order_by('-is_active')
    }
    return render(request, 'adminapp/categories.html', context=context)


# @user_passes_test(lambda u: u.is_superuser)
# def category_update(request, pk):
#     title = 'категории/редактирование'
#
#     edit_category = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         edit_form = ProductCategoryEditForm(request.POST, request.FILES, instance=edit_category)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('adminapp:category_list'))
#     else:
#         edit_form = ProductEditForm(instance=edit_category)
#     context = {
#         'title': title,
#         'form': edit_form,
#     }
#     return render(request, 'adminapp/category_update.html', context)

class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('adminapp:category_list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории/редактирование'

        return context


@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk):
    title = 'категории/удаление'

    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == "POST":
        category.is_active = False
        category.save()
        return HttpResponseRedirect(reverse("adminapp:category_list"))

    content = {
        'title': title,
        'object': category
    }

    return render(request, "adminapp/category_delete.html", content)

# product


# @user_passes_test(lambda u: u.is_superuser)
# def product_create(request, pk):
#     title = 'продукты/создание'
#     category = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         product_form = ProductEditForm(request.POST, request.files)
#         if product_form.is_valid():
#             product_form.save()
#             return HttpResponseRedirect(reverse('adminapp:product_list', args=[pk]))
#     else:
#         product_form = ProductEditForm(initial={'category': category})
#     context = {
#         'title': title,
#         'update_form': product_form,
#         'category': category
#     }
#     return render(request, 'adminapp/product_update.html', context=context)


class ProductCreateView(CreateView):
    model = Product
    template_name = 'adminapp/product_form.html'
    form_class = ProductEditForm
    # success_url = reverse_lazy('adminapp:product_list')

    def get_success_url(self):
        return reverse('adminapp:product_list', args=[self.kwargs['pk']])


# @user_passes_test(lambda u: u.is_superuser)
# def products(request, pk):
#     title = 'продукты/подробнее'
#     context = {
#         'title': title,
#         'category': get_object_or_404(ProductCategory, pk=pk),
#         'object_list': Product.objects.filter(category__pk=pk).order_by('-is_active')
#     }
#     return render(request, 'adminapp/products.html', context=context)

class ProductsListView(ListView, AccessMixin):
    model = Product
    template_name = 'adminapp/products.html'

    def get_context_data(self, *args, **kwargs):  # выбор нужной категории
        context_data = super().get_context_data(*args, **kwargs)
        context_data['category'] = get_object_or_404(ProductCategory, pk=self.kwargs.get('pk'))
        return context_data

    def get_queryset(self):  # выбор товаров нужной категории
        return Product.objects.filter(category__pk=self.kwargs.get('pk'))


# @user_passes_test(lambda u: u.is_superuser)
# def product_update(request, pk):
#     title = 'продукт/редактирование'
#     edit_product = get_object_or_404(Product, pk=pk)
#     if request.method == 'POST':
#         edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('adminapp:product_list', args=[edit_product.pk]))
#     else:
#         edit_form = ProductEditForm(instance=edit_product)
#     context = {
#         'title': title,
#         'update_form': edit_form,
#         'category': edit_product.category
#     }
#     return render(request, 'adminapp/product_update.html', context)

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'adminapp/product_form.html'
    form_class = ProductEditForm
    # success_url = reverse_lazy('adminapp:product_list')

    def get_success_url(self):
        product_item = Product.objects.get(pk=self.kwargs['pk'])
        return reverse('adminapp:product_list', args=[product_item.category_id])


# @user_passes_test(lambda u: u.is_superuser)
# def product_delete(request, pk):
#     title = 'продукт/удаление'
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == 'POST':
#         product.is_active = False
#         product.save()
#         return HttpResponseRedirect(reverse('adminapp:product_list', args=[product.category.pk]))
#     context = {
#         'title': title,
#         'product_to_delete': product
#     }
#     return render(request, 'adminapp/product_delete.html', context)

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'

    def get_success_url(self):
        product_item = Product.objects.get(pk=self.kwargs['pk'])
        return reverse('adminapp:product_list', args=[product_item.category_id])




@user_passes_test(lambda u: u.is_superuser)
def product_detail(request, pk):
    title = 'продукт/подробнее'
    product = get_object_or_404(Product, pk=pk)
    context = {
        'title': title,
        'object': product,
    }
    return render(request, 'adminapp/product_detail.html', context)
