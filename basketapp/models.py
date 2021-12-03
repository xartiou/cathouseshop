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
    # когда переобновили
    # updated_at = models.DateTimeField(auto_now=True)

