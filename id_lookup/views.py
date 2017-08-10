from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Security
from .utility import logger
import json



# Create your views here.
def fbview(request):
	"""
	Create a json response.
	"""
	data = {'foo':'bar', 'balance':88.8}
	return HttpResponse(json.dumps(data), content_type='application/json')



def security_lookup(request):
	"""
	Find a security based on the security_id_type and security_id
	"""
	security_id_type = request.GET.get('security_id_type', '')
	security_id = request.GET.get('security_id', '')
	logger.debug('security_lookup(): security_id_type={0}, security_id={1}'.\
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