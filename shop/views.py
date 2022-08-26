from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.db.models import Q
from django.shortcuts import render,get_object_or_404
from . import views

# Create your views here.
from .models import *

def home(request,c_slug=None):
        c_page=None
        prd=None
        if c_slug!=None:
            c_page=get_object_or_404(Category,slug=c_slug)
            prd=Product.objects.filter(category=c_page, available=True)
        else:

            prd = Product.objects.all().filter(available=True)

        catg=Category.objects.all()
        paginator=Paginator(prd,8)
        try:
            page=int(request.GET.get('page','1'))
        except:
            page=1

        try:
            pro=paginator.page(page)
        except (EmptyPage,InvalidPage):
            pro=paginator.page(paginator.num_pages)

        return render(request,'index.html',{'prd': prd,'ct':catg,'page':pro})

def productDetails(request,c_slug,product_slug):

        try:
            prodt=Product.objects.get(category__slug=c_slug,slug=product_slug)
        except Exception as e:
            raise e
        return render(request,'detail.html',{'pr':prodt})

def searching(request):
        prod=None
        quary=None
        if 'q' in request.GET:
            quary=request.GET.get('q')
            prod=Product.objects.all().filter(Q(name__contains=quary)|Q(desc__contains=quary))

        return render(request,'search.html',{'qr':quary,'pr':prod})