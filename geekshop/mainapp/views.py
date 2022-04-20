import json
from django.shortcuts import render

from mainapp.models import Product


def products(requests):

    with open('links_header.json', 'r', encoding='utf-8') as f:
        links_header_json = f.read()

    links_header = json.loads(links_header_json)


    products_70 = Product.objects.all()[5:]
    products_270 = Product.objects.all()[1:4]

    context = {
        'title': 'каталог',
        'links_header': links_header,
        'object': Product.objects.get(name='Фонтан-1'),
        'products_70': products_70,
        'products_270': products_270,
    }
    return render(requests, 'mainapp/products.html', context)

