from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.http import JsonResponse

# Create your views here.
def home(request):
    trending_product = Product.objects.filter(trending=1)
    context={'trending_product':trending_product}
    return render(request,'store/index.html',context)

def collections(request):
    category = Category.objects.filter(status=0)
    context = {'category':category}
    return render(request,'store/collections.html',context)   

def collectionsview(request,slug):
    if(Category.objects.filter(slug=slug,status=0)):
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'products':products,'category':category}
        return render(request,'store/products/index.html',context)
    else:
        messeges.warning(request,'No such category found!')
        return redirect('collections')

def productview(request,cate_slug,prod_slug):
    if(Category.objects.filter(slug=cate_slug,status=0)):
        if(Product.objects.filter(slug=prod_slug,status=0)):
            products=Product.objects.filter(slug=prod_slug,status=0).first
            context = {'products':products}
        else:
          messages.error(request,'No such product found!')
          return redirect('collections')  
    else:
        messages.error(request,'No such category found!')
        return redirect('collections') 
    return render(request,'store/products/view.html',context)           

def productlistAjax(request):
    products = Product.objects.filter(status=0).values_list('name',flat=True)
    productsList = list(products)
    return JsonResponse(productsList, safe=False)  
     

def searchproduct(request):
    if request.method == "POST":
        searchedterm = request.POST.get('productsearch')

        # Check if the search term is empty
        if not searchedterm:
            return redirect(request.META.get('HTTP_REFERER', '/'))  

        # Attempt to fetch the product based on the search term
        product = Product.objects.filter(name__icontains=searchedterm).first()
        if product:
            return redirect(f'collections/{product.category.slug}/{product.slug}')
        else:
            messages.info(request, "No product matched your search")
            return redirect(request.META.get('HTTP_REFERER', '/'))
    
    # Fallback redirect for non-POST requests
    return redirect('home')
