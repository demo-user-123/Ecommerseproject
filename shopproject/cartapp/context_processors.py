from .models import Cart, Cart_Item
from .views import _cart_id


def counter(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(Cart_id=_cart_id(request))
            cart_items = Cart_Item.objects.all().filter(Cart=cart[:1])
            for car_item in cart_items:
                item_count += car_item.Quantity
        except Cart.DoesNotExist:
            item_count = 0
    return dict(item_count=item_count)
