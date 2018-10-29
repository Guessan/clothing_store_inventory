from django.shortcuts import render, HttpResponse

from .models import Clothes

# Create your views here.
def login(requests):
	return render(requests, 'ClothingInventoryProject/login.html')

def listProduct(requests):
	queryset = Clothes.objects.all()
	context = {
		'Product': queryset
	}
	return render(requests, 'ClothingInventoryProject/list_inventory.html', context)