# My first view

from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from datetime import datetime

import logging
logger = logging.getLogger(__name__)



def hello(request):
	return HttpResponse('<h1>Hello, World</h1>')



def form_serial(request):
	"""
	Return a serial string based on current time. Say the time is
	2017-8-24 16:15:24, then return 20170824161524.
	"""
	logger.info('form_serial(): enter')
	return HttpResponse(datetime.now().strftime('%Y%m%d%H%M%S'))

