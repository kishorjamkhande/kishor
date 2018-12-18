from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'availabel', 'created', 'updated']
    list_editable = ['price', 'stock', 'availabel']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20

admin.site.register(Product, ProductAdmin)
