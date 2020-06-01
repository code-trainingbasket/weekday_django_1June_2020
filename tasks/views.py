from django.shortcuts import render

# Create your views here.
from .models import Employee

def home(request):
	users = ['Rishabh','Sumit','Vishal']
	return render(request,'index.html',{'users':users})


def employees(request):
	allemployees = Employee.objects.all()
	context = {'allemployees':allemployees}
	return render(request,'employees.html',context)