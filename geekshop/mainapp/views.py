import random

from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_products(num):
    products = Product.objects.all()
    return random.sample(list(products), num)


def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]


def get_same_product(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk).order_by('price')
    return same_products


def products(request, pk=None, page=1):
    title = 'каталог'
    links_menu = ProductCategory.objects.all()
    basket = get_basket(request.user)

    products = Product.objects.all().order_by('price')
    hot_product = get_hot_product()
    same_products = get_same_product(hot_product)

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
            'basket': basket,
        }

        return render(request, 'mainapp/products_list.html', context)

    paginator = Paginator(same_products, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context = {
        'title': title,
        'links_menu': links_menu,

        'products_3': get_products(3),
        'hot_product': hot_product,
        'same_products': products_paginator,
        'basket': basket,
        'products': products,
    }
    return render(request, 'mainapp/products.html', context)


def product(request, pk):
    title = 'детали продукта'
    links_menu = ProductCategory.objects.all()
    basket = get_basket(request.user)

    product = get_object_or_404(Product, pk=pk)
    hot_product = get_hot_product()
    same_products = get_same_product(hot_product)

    context = {
        'title': title,
        'links_menu': links_menu,
        'product': product,
        'same_products': same_products,
        'basket': basket,
    }
    return render(request, 'mainapp/product.html', context)
