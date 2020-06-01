from django.db import models

# Create your models here.
g_choices = (
				('M','MALE'),
				('F','FEMALE')
			)

class Employee(models.Model):

	name = models.CharField(max_length=100)
	joining_date = models.DateField()
	designation = models.CharField(max_length=100)
	phonenumber = models.BigIntegerField()
	gender = models.CharField(max_length = 6,choices = g_choices)

	# For an informal representation of our object
	def __str__(self):
		return self.name