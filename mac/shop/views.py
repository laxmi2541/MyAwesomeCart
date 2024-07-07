from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from . import forms
from .models import Product


def index(request):
    return render(request, 'shop/index.html')


def about(request):
    return HttpResponse("We are at about")


def contact(request):
    return HttpResponse("We are at contact")


def tracker(request):
    return HttpResponse("We are at tracker")


def search(request):
    return HttpResponse("We are at search")


def productview(request):
    return HttpResponse("We are at product view")


def add_product(request):
    if request.method == "POST":
        form = forms.ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/shop/products")

    else:
        form = forms.ArticleForm()

    return render(request, "shop/product_form.html", {"form": form})


def list_products(request):
    if request.method == "GET":
        products = Product.objects.all()
        return render(request, 'shop/list_products.html', {'products': products})


def checkout(request):
    return HttpResponse("We are at checkout")
