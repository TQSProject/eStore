from django.contrib import admin

from stores.models import Product, ProductTag, Store

# Register your models here.
admin.site.register(ProductTag)
admin.site.register(Product)
admin.site.register(Store)
