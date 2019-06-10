from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_cart(request):
    """
    Allows users to view products, total price and quantities bought
    """
    return render(request, "cart.html")
    
    
def add_to_cart(request, id):
    """
    Allows users to add products of a specified quantity to their cart contents
    """
    quantity = int(request.POST.get("quantity"))
    cart = request.session.get("cart", {})
    cart[id] = cart.get(id, quantity)
    
    request.session["cart"] = cart
    
    return redirect(reverse("products"))
    
    
def adjust_cart(request, id):
    """
    Allows users to update the quantities of their cart contents
    """
    quantity = int(request.POST.get("quantity"))
    cart = request.session.get("cart", {})
   
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
        
    request.session["cart"] = cart
    
    return redirect(reverse("view_cart"))
    