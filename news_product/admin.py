from django.contrib import admin
from .models import Pricing, Index

@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
   

@admin.register(Index)
class IndexAdmin(admin.ModelAdmin):
   