from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products(request):
    """
    Returns all products of the Product type in the website
    """
    products = Product.objects.all()
    return render(request, "products.html", { "products": products } )
    
