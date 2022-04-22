from django.shortcuts import render

from basketapp.models import Basket
from mainapp.models import Product


def index(request):
    products = Product.objects.all()[:3]
    basket = []
    basket_price = 0
    basket_quantity = 0

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        for el in basket:
            basket_price += (el.product.price * el.quantity)
            basket_quantity += el.quantity


    context = {
        'title': 'главная',
        'products': products,
        'basket': basket,
        'basket_price': basket_price,
        'basket_quantity': basket_quantity,
    }

    return render(request, 'geekshop/index.html', context)


def contacts(request):
    basket = []
    basket_price = 0
    basket_quantity = 0

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        for el in basket:
            basket_price += (el.product.price * el.quantity)
            basket_quantity += el.quantity


    context = {
        'title': 'контакты',
        'basket': basket,
        'basket_price': basket_price,
        'basket_quantity': basket_quantity,
    }
    return render(request, 'geekshop/contact.html', context)
