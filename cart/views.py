from django.shortcuts import render, redirect,get_object_or_404

# Create your views here.
from .models import *
from shop.models import *
from django.core.exceptions import ObjectDoesNotExist



def cartDetails(request,tot=0,count=0):
    c_items = None

    try:
        ct = CartList.objects.get(cart_id=cart_id(request))
        c_items = Items.objects.filter(cart=ct,active=True)
        for i in c_items:
            tot+=(i.products.price*i.quantity)
            count +=i.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',{ 'c':c_items,'tot':tot,'count':count })

def cart_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id= request.session.create()
    return ct_id

def add_cart(request,product_id):
    prod=Product.objects.get(id=product_id)
    try:
        ct=CartList.objects.get(cart_id=cart_id(request))
    except CartList.DoesNotExist:
        ct=CartList.objects.create(cart_id=cart_id(request))
        ct.save()
    try:
        c_items=Items.objects.get(products=prod,cart=ct)
        if c_items.quantity < c_items.products.stock:
            c_items.quantity+=1
            c_items.save()
    except Items.DoesNotExist:
        c_items=Items.objects.create(products=prod,quantity=1,cart=ct)
        c_items.save()
    return redirect('cartdetails')

def min_cart(request,product_id):
    ct=CartList.objects.get(cart_id=cart_id(request))
    prod=get_object_or_404(Product,id=product_id)
    c_items=Items.objects.get(products=prod,cart=ct)
    if c_items.quantity > 1:
        c_items.quantity-= 1
        c_items.save()
    else:
        c_items.delete()
    return redirect("cartdetails")

def delete_cart(request,product_id):
    ct = CartList.objects.get(cart_id=cart_id(request))
    prod = get_object_or_404(Product, id=product_id)
    c_items = Items.objects.get(products=prod, cart=ct)
    c_items.delete()
    return redirect("cartdetails")
