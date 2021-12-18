from django.conf import settings
from django import template

register = template.Library()  # регистратор фильтров и тегов


@register.filter(name='media_for_products')  # декоратор регистратора
def media_for_products(img_path):
    if not img_path:
        img_path = 'products_images/product-61.jpg'
    return f'{settings.MEDIA_URL}{img_path}'


@register.filter(name='media_for_users')
def media_for_users(img_path):
    if not img_path:
        img_path = 'users_avatars/default.png'
    return f'{settings.MEDIA_URL}{img_path}'
