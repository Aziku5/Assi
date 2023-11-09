from django.contrib import admin
from .models import TagCL, CustomerCL, ProductCL, OrderCL

admin.site.register(TagCL)
admin.site.register(CustomerCL)
admin.site.register(ProductCL)
admin.site.register(OrderCL)
