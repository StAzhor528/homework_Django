from django.shortcuts import render


def products(requests):
    return render(requests, 'mainapp/products.html')

