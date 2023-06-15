from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'app/index.html')


def cus(request):
    return render(request, 'app/customer_analysis.html')


def product(request):
    return render(request, 'app/hot_product.html')

def propor(request):
    return render(request, 'app/proportion_and_subclass.html')

def nation(request):
    return render(request, 'app/national_profile.html')

def deli(request):
    return render(request, 'app/delivery_time.html')
def price(request):
    return render(request, 'app/price_analysis.html')
def regional(request):
    return render(request, 'app/regional_statistics.html')


