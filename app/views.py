from django.shortcuts import redirect, render
from .models import *
from .form import *


def products(request):
    template = 'app/product.html'
    allproduct = product.objects.all()
    context = {'allproduct':allproduct}
    return render (request, template, context)

def detail(request, pk):
    template = 'app/detail.html'
    productobj = product.objects.get(id=pk)
    context = {'productobj':productobj}
    return render (request, template, context)

def add(request):
    template = 'app/addproduct.html'
    form = ProductForm()
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    context = {'form':form}
    return render(request, template, context)

def edit(request, pk):
    template = 'app/addproduct.html'
    productedit = product.objects.get(id=pk)
    form= ProductForm(instance=productedit)
    if request.method=='POST':
        form = ProductForm(request.POST, instance=productedit)
        if form.is_valid():
            form.save()
        return redirect('home')
    context ={'productediit':productedit, 'form':form}
    return render(request, template, context)

def delete(request, pk):
    template = 'app/deleteproduct.html'
    productdelete = product.objects.get(id=pk)
    if request.method=='POST':
        productdelete.delete()
        return redirect('home')
    context = {'productdelete':productdelete}
    return render(request, template, context)