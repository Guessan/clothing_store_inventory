from django.contrib import admin

# Register your models here.
from .models import Clothes

# puts our columns into a tuple
class ClothesAdmin(admin.ModelAdmin):
    list_display = ("Brand",
                    "Color",
                    "Price",
                    "Size",
                    "Quantity",
                    "Gender",
                    "Type",
                    )
    # create search bar in admin
    search_fields = ["Brand",
                     "Color",
                     "Price",
                     "Size",
                     "Quantity",
                     "Gender",
                     "Type",]

admin.site.register(Clothes, ClothesAdmin)