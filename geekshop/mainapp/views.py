from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory


def products(request, pk=None):
    title = 'каталог'
    links_menu = ProductCategory.objects.all()
    basket = []
    basket_price = 0
    basket_quantity = 0

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        for el in basket:
            basket_price += (el.product.price * el.quantity)
            basket_quantity += el.quantity

    products = Product.objects.all().order_by('price')
    products_70 = Product.objects.all()[5:]
    products_270 = Product.objects.all()[1:4]
    same_products = Product.objects.all()[1:6]

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        context = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'same_products': same_products,
            'basket': basket,
            'basket_price': basket_price,
            'basket_quantity': basket_quantity,
        }

        return render(request, 'mainapp/products_list.html', context)

    context = {
        'title': title,
        'links_menu': links_menu,
        'object': Product.objects.get(name='Фонтан-1'),
        'products_70': products_70,
        'products_270': products_270,
        'same_products': same_products,
        'basket': basket,
        'products': products,
        'basket_price': basket_price,
        'basket_quantity': basket_quantity,
    }
    return render(request, 'mainapp/products.html', context)
