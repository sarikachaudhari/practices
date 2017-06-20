from .models import *
import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render_to_response

def get_employee(request):
	employee = Employee.objects.all()
	emp_list = []
	for emp in employee:
		dict = {
					"name":emp.name,
					"img":emp.file.url

		}
		emp_list.append(dict)
	return HttpResponse(json.dumps({"status":True,"validation":'get Product',"emp_list":dict}), content_type="application/json")

def add_employee(request):
	jsonobj = json.loads(request.body)
	
	name = jsonobj.get("name")
	file = jsonobj.get("file")

	try:
		employee = Employee()
		employee.name = name
		employee.file = file
		employee.save()
		return HttpResponse(json.dumps({"status":True,"validation":'add employee successfully'}), content_type="application/json")
	except Exception as e:
		print e
		return HttpResponse(json.dumps({"status":True,"validation":'failed to add employee'}),content_type="application/json")
		

