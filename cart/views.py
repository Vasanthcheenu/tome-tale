
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from cart.cart import Cart
from webapp.models import Product

# Create your views here.
def cart_summary(request):
    cart=Cart(request)
    cart_products=cart.get_prods
    quantities=cart.get_quants
    totals = cart.cart_total()
    return render(request, "cart_summary.html", {"cart_products":cart_products, "quantities":quantities,"totals":totals})

def cart_add(request):
    cart=Cart(request) #get the cart(cart.py)
    if request.POST.get('action') == 'post': #django understands POST & script understands the post 
        product_id = int(request.POST.get('product_id')) #get the product id
        product_qty=int(request.POST.get('product_qty'))

        product = get_object_or_404(Product,id=product_id) #lookup product in db
        cart.add(product=product,quantity=product_qty) #save the session 
        cart_quantity = cart.__len__()
        #response = JsonResponse({'Product Name:' : product}) #return response
        response = JsonResponse({'qty' : cart_quantity})
        messages.success(request,('Added'))
        return response
    

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id')) #get the product id.
        product_qty = int(request.POST.get('product_qty')) #get qty
        cart.update(product=product_id, quantity=product_qty)
        response = JsonResponse({'qty':product_qty})
        messages.success(request,('Upadate'))
        return response

def cart_delete(request):
    cart=Cart(request)
    if request.POST.get('action')=='post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        response=JsonResponse({'product':product_id})
        messages.success(request,('Deleted'))
        return response