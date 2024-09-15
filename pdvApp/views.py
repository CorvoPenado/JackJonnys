# pdvApp/views.py

from django.shortcuts import render, redirect
from .models import Product, Sale
from .forms import SaleForm, ProductForm

def home(request):
    products = Product.objects.all()
    return render(request, 'pdvApp/home.html', {'products': products})

def register_sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SaleForm()
    return render(request, 'pdvApp/register_sale.html', {'form': form})

def sales_report(request):
    sales = Sale.objects.all()
    total_gasto = sum(sale.total_price for sale in sales)
    return render(request, 'pdvApp/sales_report.html', {'sales': sales, 'total_gasto': total_gasto})

def register_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'pdvApp/register_product.html', {'form': form})
