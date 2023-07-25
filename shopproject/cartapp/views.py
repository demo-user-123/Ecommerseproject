from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import HttpResponse
from shopapp.models import Category,Products
from .models import Cart,Cart_Item
from django.core.exceptions import ObjectDoesNotExist


# Create
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
        return cart


def add_cart(request, product_id):
    product = Products.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(Cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            Cart_id=_cart_id(request)
        )
        cart.save()
    try:
        cartitem = Cart_Item.objects.get(Product=product, Cart=cart)
        if cartitem.Quantity < cartitem.Product.stock:
            cartitem.Quantity += 1
        cartitem.save()
    except Cart_Item.DoesNotExist:
        cartitem = Cart_Item.objects.create(
            Product=product,
            Quantity=1,
            Cart=cart
        )
        cartitem.save()
    return redirect('cart_app:cart_details')


def cart_details(request, total=0, counter=0, cartitem=None):
    try:
        cart = Cart.objects.get(Cart_id=_cart_id(request))
        cartitem = Cart_Item.objects.filter(Cart=cart, active=True)
        for car in cartitem:
            total += (car.Product.price * car.Quantity)
            counter += car.Quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', dict(cartitems=cartitem, total=total, counter=counter))


def cart_remove(request, product_id):
    cart = Cart.objects.get(Cart_id=_cart_id(request))
    product = get_object_or_404(Products, id=product_id)
    cart_item = Cart_Item.objects.get(Product=product, Cart=cart)
    if cart_item.Quantity > 1:
        cart_item.Quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_app:cart_details')


def deletion(request, product_id):
    cart = Cart.objects.get(Cart_id=_cart_id(request))
    product = get_object_or_404(Products, id=product_id)
    cart_item = Cart_Item.objects.get(Product=product, Cart=cart)
    cart_item.delete()
    return redirect('cart_app:cart_details')
