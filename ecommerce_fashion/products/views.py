from django.shortcuts import render
from products.models import Product
from products.templatetags import chunks
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    featured_products=Product.objects.order_by('priority')[:4]
    latest_products=Product.objects.order_by('-id')[:4]

    context={'featured_products':featured_products,'latest_products':latest_products}
    return render(request,'index.html',context)

def list_products(request):

    page=1
    if request.GET:
        page=request.GET.get('page',1)
    product_list=Product.objects.order_by('priority')
    product_paginator=Paginator(product_list,12)
    product_list=product_paginator.get_page(page)
    context={'product_list':product_list}
    return render(request,'product.html',context)

def detail_product(request,pk):
    product=Product.objects.get(id=pk)
    context={'product':product}

    return render(request,'product_detail.html',context)