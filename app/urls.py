from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customer', views.cus, name='customer_analysis'),
    path('proportion', views.propor, name='proportion_and_subclass'),
    path('product', views.product, name='hot_product'),
    path('national', views.nation, name='national_profile'),
    path('delivery', views.deli, name='delivery_time'),
    path('price', views.price, name='price_analysis'),
]