from django.contrib import admin

# Register your models here.
from .models import Clothes

# puts our columns into a tuple
class ClothesAdmin(admin.ModelAdmin):
    # create a display for our items
    list_display = ("Brand",
                    "Color",
                    "Price",
                    "Size",
                    "Quantity",
                    "Gender",
                    "Type",
                    )
    # create a filter for a category
    list_filter = ("Brand",
                    "Color",
                    "Size",
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