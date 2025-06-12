from django.db import models    #for sql
#from djongo import models     #for mongodb nosql



class Order(models.Model):
	total = models.FloatField()
	customer_name = models.CharField(max_length=100)
	customer_email = models.CharField(max_length=100)
	#items = models.ListField(default=None)
	items = models.JSONField(default=list)


	def __str__(self):
		return self.customer_email


	class Meta:
		verbose_name = "Buyurtmachi_"
