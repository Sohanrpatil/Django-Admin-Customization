from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Product

def change_rating(modeladmin, request, queryset):
    queryset.update(rating = 'e')

change_rating.short_description = "Mark Selected Products as Excellent"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'mfg_date', 'rating')
    list_filter = ('mfg_date', )
    actions = [change_rating]

admin.site.register(Product, ProductAdmin)
admin.site.site_header = "Django Admin Customization "