from django.shortcuts import render

from mainapp.views import get_basket, get_products


def index(request):
    products = get_products(3)
    basket = get_basket(request.user)

    context = {
        'title': 'главная',
        'products': products,
        'basket': basket,
    }

    return render(request, 'geekshop/index.html', context)


def contacts(request):
    basket = get_basket(request.user)
    context = {
        'title': 'контакты',
        'basket': basket,
    }
    return render(request, 'geekshop/contact.html', context)
