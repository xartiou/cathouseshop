from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "mainapp/index.html")


def products(request):
    return render(request, "mainapp/products.html")


def contact(request):
    return render(request, "mainapp/contact.html")


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
