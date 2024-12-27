from django.contrib import admin
from  .models.product import product
from  .models.category import Category
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    class Meta:
        model = product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(product, ProductAdmin)
admin.site.register(Category)
# Register your models here.
