from django.db import models
from django.conf import settings
from mainapp.models import Product


class Basket(models.Model):
    # кто положил в корзину
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    # что положил в корзину
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # сколько
    quantity = models.PositiveSmallIntegerField(default=0)

    # когда добавили в корзину
    add_daytime = models.DateTimeField(auto_now_add=True)

    # когда обновили
    # updated_at = models.DateTimeField(auto_now=True)

    @property  # декоратор преобразовывает метод в атрибут
    def product_cost(self):
        # стоимость товаров в одной корзинке
        return self.quantity * self.product.price

    @property
    def total_quantity(self):  # получаем полную корзину пользователя
        _items = Basket.objects.filter(user=self.user)
        return sum(list(map(lambda x: x.quantity, _items)))

    @property
    def total_cost(self):    # общая стоимость товаров
        _items = Basket.objects.filter(user=self.user)
        return sum(list(map(lambda x: x.product_cost, _items)))

