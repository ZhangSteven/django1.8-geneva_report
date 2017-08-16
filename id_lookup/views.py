from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Security
import json
import logging

# to make certain views exempt from security protection
from django.views.decorators.csrf import csrf_exempt

# Get an instance of a logger (needs to define the logger first in settings.py)
logger = logging.getLogger('__name__')



# Create your views here.
def fbview(request):
	"""
	Create a json response.
	"""
	data = {'foo':'bar', 'balance':88.8}
	return HttpResponse(json.dumps(data), content_type='application/json')



@csrf_exempt	# CAUTION! this view is not protected by CSRF, any one can
				# change your site's data
def security_lookup(request):
	"""
	Find a security based on the security_id_type and security_id
	"""
	logger.info('security_lookup(): enter')

	if request.method == 'GET':
		security_id_type = request.GET.get('security_id_type', '')
		security_id = request.GET.get('security_id', '')
		logger.debug('security_lookup() get: security_id_type={0}, security_id={1}'.\
						format(security_id_type, security_id))

		if security_id_type == '' or security_id == '':
			logger.error('security_lookup(): invalid security_id_type or security_id')
			raise Http404()

		try:
			s = Security.objects.get(security_id_type=security_id_type,\
										security_id=security_id)
			return HttpResponse(s.to_json(), content_type='application/json')

		except:
			logger.exception('security_lookup()')
			raise Http404()

	elif request.method == 'PUT':
		logger.debug('security_lookup() put')
		return HttpResponse('put ok')

	else:
		logger.debug('security_lookup() unknown method')
		raise Http404()