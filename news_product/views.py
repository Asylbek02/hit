from django.shortcuts import render
from .models import Pricing

def pricing_view(request):
    products = Pricing.objects.all()
    return render(request, 'pricing.html', {'products': products})
