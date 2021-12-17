from django.conf import settings



def media_for_products(img_path):
    if not img_path:
        img_path = 'products_images/default.jpg'

    from django.conf import settings
    return f'{settings.MEDIA_URL}{img_path}'


def media_for_users(img_path):
    if not img_path:
        img_path = 'users_avatars/default.jpg'

    from django.conf import settings
    return f'{settings.MEDIA_URL}{img_path}'

