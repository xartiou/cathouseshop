from authapp.forms import ShopUserEditForm
from authapp.models import ShopUser


class ShopUserAdminEditForm(ShopUserEditForm):  # форма для работы с пользователем
    class Meta:
        model = ShopUser
        fields = '__all__'

