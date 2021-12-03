from django.urls import path
from basketapp import views as basket

app_name = 'basketapp'

urlpatterns = [
    # отображаем корзину
    path('', basket.basket, name='basket'),
    # добавляем в корзину
    path('add/,<int:pk>/', basket.add, name='add'),
    # удаляем из корзины
    path('remove/<int:pk>/', basket.remove, name='remove')
]
