
from store.models.customer import Customer
from django.views import View
from django.shortcuts import render, redirect
from store.models.category import Category
from store.models.product import Product
def search(request):
    q=request.GET['q']
    data=Product.objects.filter(name__icontains=q).order_by('-id')
    categories=Category.get_all_categories()
    return render(request,'search.html',{'data':data,'categories':categories})