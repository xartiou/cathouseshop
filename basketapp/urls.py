from django.urls import path
from basketapp import views as basketapp

app_name = 'basketapp'

urlpatterns = [
    # отображаем корзину
    path('', basketapp.basket, name='basket'),
    # добавляем в корзину
    path('add/,<int:pk>/', basketapp.add, name='add'),
    # удаляем из корзины
    path('remove/<int:pk>)/', basketapp.basket_remove, name='remove'),
]