from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registrar-venda/', views.register_sale, name='register_sale'),
    path('relatorio-vendas/', views.sales_report, name='sales_report'),
    path('registrar-produto/', views.register_product, name='register_product'),
]