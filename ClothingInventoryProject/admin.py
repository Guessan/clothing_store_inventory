from django.contrib import admin

# Register your models here.
from .models import Clothes

# add to our site
admin.site.register(Clothes)