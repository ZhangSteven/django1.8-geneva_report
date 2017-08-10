from django.shortcuts import render
from django.http import HttpResponse
import json



# Create your views here.
def fbview(request):
	"""
	Create a json response.
	"""
	data = {'foo':'bar', 'balance':88.8}
	return HttpResponse(json.dumps(data), content_type='application/json')