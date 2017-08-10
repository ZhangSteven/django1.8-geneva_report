# My first view

from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render



def hello(request):
	return HttpResponse('<h1>Hello, World</h1>')
