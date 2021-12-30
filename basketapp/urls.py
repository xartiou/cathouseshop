from django.urls import path

import basketapp.views as basketapp
from basketapp import views as basket

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.basket, name='basket'),  # отображаем корзину
    path('add/<int:pk>/', basketapp.basket_add, name='add'),  # добавляем в корзину
    path('remove/<int:pk>/', basketapp.remove, name='remove'),  # удаляем из корзины
    path('edit/<int:pk>/<int:quantity>/', basketapp.edit, name='edit')  # редактируем корзину

]
