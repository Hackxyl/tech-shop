from django.contrib import admin
from .models import product, contactMessage, about

# Register your models here.
admin.site.register(product)
admin.site.register(contactMessage)
admin.site.register(about)
