from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Product


def home(request):
    products = Product.objects.all()

    # Kategoriye göre filtreleme
    category = request.GET.get('category')
    if category:
        products = products.filter(category=category)

    # İsimle arama
    search_query = request.GET.get('search_query')
    if search_query:
        products = products.filter(name__icontains=search_query)

    context = {'products': products, 'selected_category': category}
    return render(request, 'home.html', context)

def category_filter(request, category):
    products = Product.objects.filter(category=category)
    context = {'products': products, 'selected_category': category}
    return render(request, 'home.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product}
    return render(request, 'product_detail.html', context)