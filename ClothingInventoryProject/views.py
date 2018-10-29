<<<<<<< HEAD
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Hellooooo')


def homepage(request):
    #return HttpResponse('Hellooooo')
    return render(request, 'ClothingInventoryProject/homepage.html')

=======
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
>>>>>>> master
