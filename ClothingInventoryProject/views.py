from django.shortcuts import render
from django.http import HttpResponse
from .models import Clothes
from django.db.models import Q # allows to utilize complex query lookups
# Create your views here.
def index(request):
    return HttpResponse('Hellooooo')

def layout(request):
	queryset = Clothes.objects.all()

	context = {
		'cloth': queryset,
		
	}
	return render(request, 'ClothingInventoryProject/layout.html', context)

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

# renders search form
def search_form(request):
	return render(request, 'ClothingInventoryProject/search_form.html')

# handles data and looks for matches in database
def search(request):
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		# Complex queries using "&" and "|", added order_by price functionality
		clothes = Clothes.objects.filter(Q(Brand__icontains=q) | Q(Color__icontains=q) | Q(Gender__icontains=q) | Q(Type__icontains=q)).order_by("Price")
		return render(request, 'ClothingInventoryProject/search_results.html',
						{'clothes': clothes, 'query': q})
	else:
		message = 'You submitted an empty form'

	return HttpResponse(message)

def bad_search(request):
	message = "You searched for: {}".format(request.GET['q'])
	return HttpResponse(message)

def brand(request):
	# Grab unique brands
	queryset = Clothes.objects.values("Brand").distinct()
	context = {
		'cloth': queryset
	}
	return render(request, 'ClothingInventoryProject/brand.html', context)

def color(request):
	# Grab unique colors
	queryset = Clothes.objects.values("Color").distinct()
	context = {
		'cloth': queryset
	}
	return render(request, 'ClothingInventoryProject/color.html', context)