from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Products, Category
from django.core.paginator import Paginator, EmptyPage, InvalidPage


# Create your views here.
def allProdCat(request, c_slug=None):
    c_page = None
    products_list = None
    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products_list = Products.objects.all().filter(category=c_page, available=True)
    else:
        products_list = Products.objects.all().filter(available=True)
    new = Paginator(products_list, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = new.page(page)
    except(EmptyPage, InvalidPage):
        products = new.page(new.num_pages)

    return render(request, "category.html", {'cat': c_page, 'pro': products})


def proDetail(request, c_slug, pro_slug):
    try:
        prodet = Products.objects.get(category__slug=c_slug, slug=pro_slug)
    except  Exception as e:
        raise e
    return render(request, 'prodetail.html', {'product': prodet})
