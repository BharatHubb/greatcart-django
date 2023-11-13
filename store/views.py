from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
# Create your views here.


def store(request, category_slug=None):
    categories = None
    product = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        product = Product.objects.filter(category=categories, is_availabel=True)
        produ_count = product.count()
        context = {
        'products': product, 
        'product_count': produ_count, 
        }
    else:
        product = Product.objects.all().filter(is_availabel=True)
        pro_count = Product.objects.count()
        context = {
            'products': product, 
            'product_count': pro_count, 
        }
    return render(request, "store/store.html", context)

def product_details(request,category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    context = {
        'signle_product': single_product,
    }
    return render(request, 'store/product_details.html', context)