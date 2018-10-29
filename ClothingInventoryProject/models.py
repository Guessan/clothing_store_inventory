from django.db import models

# Create your models here.
from django.db import models

class Clothes(models.Model): # ProductCategory
	Brand 		= models.CharField(max_length=20)
	Color 		= models.CharField(max_length=20)
	Price 		= models.DecimalField(decimal_places=2, max_digits=20, default=0.00) # self-explanatory
	Size		= models.CharField(max_length=20)
	Quantity 	= models.IntegerField()
	Gender 		= models.CharField(max_length=6)
	Type 		= models.CharField(max_length=10)

	def __str__(self):
		# Going name "product object" according to title
		return self.Brand