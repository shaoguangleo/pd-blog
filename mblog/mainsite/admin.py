from django.contrib import admin
from .models import Post
from .models import Product

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'price', 'size')

admin.site.register(Post, PostAdmin)
admin.site.register(Product, ProductAdmin)