#from djongo import models #for mongodb nosql
from django.db import models



class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
	       return self.name


	class Meta:
	      verbose_name = "Kategoriya_"



class Product(models.Model):
	category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="category")
	name = models.CharField(max_length=100)
	price = models.FloatField()
	description = models.TextField()

	def __str__(self):
	    return self.name

	class Meta:
	    verbose_name = "Mahsulot_"
