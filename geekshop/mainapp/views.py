import json
from django.shortcuts import render


def products(requests):

    with open('links_header.json', 'r', encoding='utf-8') as f:
        links_header_json = f.read()

    links_header = json.loads(links_header_json)

    with open('links_menu.json', 'r', encoding='utf-8') as f:
        links_menu_json = f.read()

    links_menu = json.loads(links_menu_json)

    context = {'links_menu': links_menu,
               'links_header': links_header}
    return render(requests, 'mainapp/products.html', context)

