from django.shortcuts import render
import json


def index(request):
    with open('links_header.json', 'r', encoding='utf-8') as f:
        links_header_json = f.read()

    links_header = json.loads(links_header_json)

    context = {'links_header': links_header}

    return render(request, 'geekshop/index.html', context)


def contacts(request):
    with open('links_header.json', 'r', encoding='utf-8') as f:
        links_header_json = f.read()

    links_header = json.loads(links_header_json)

    context = {'links_header': links_header}
    return render(request, 'geekshop/contact.html', context)