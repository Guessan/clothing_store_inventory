from django.shortcuts import render
from django.http import HttpResponse
from .models import Clothes
# Create your views here.
def index(request):
    return HttpResponse('Hellooooo')


def homepage(request):
	#return HttpResponse('Hellooooo')
	queryset = Clothes.objects.all()
	context = {
		'cloth': queryset
	}
	return render(request, 'ClothingInventoryProject/homepage.html', context)


# Create your views here.
def login(requests):
	return render(requests, 'ClothingInventoryProject/login.html')

def listProduct(requests):
	# queryset = Clothes.objects.all()
	return render(requests, 'ClothingInventoryProject/list_inventory.html')
	
#the url for about page
def about(request):
	return render(request, 'ClothingInventoryProject/about.html')

def search_form(request):
	return render(request, 'ClothingInventoryProject/search_form.html')

def search(request):
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		clothes = Clothes.objects.filter(Brand__icontains=q)
		return render(request, 'ClothingInventoryProject/search_results.html',
						{'clothes': clothes, 'query': q})
	else:
		message = 'You submitted an empty form'

	return HttpResponse(message)

def bad_search(request):
	message = "You searched for: {}".format(request.GET['q'])
	return HttpResponse(message)