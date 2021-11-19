from django.shortcuts import render


# Create your views here.
def index(request):
    menu = {'title': 'cathouseshop'}
    return render(request, "mainapp/index.html", menu)


def products(request):
    menu = {'title': 'cathouseshop'}
    return render(request, "mainapp/products.html", menu)


def contact(request):
    menu = {'title': 'cathouseshop'}
    return render(request, "mainapp/contact.html", menu)


def context(request):
    context = {
        'title': 'test context',
        'header': 'Добро пожаловать на сайт',
        'username': 'juan',
        'products': [
            {'name': 'Стулья', 'price': 9999},
            {'name': 'Диваны', 'price': 99999},
            {'name': 'Столы', 'price': 19999}
        ]
    }
    return render(request, "mainapp/text_context.html", context)

def menu(request):
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    return render(request, 'inc_categories_menu.html', links_menu)
