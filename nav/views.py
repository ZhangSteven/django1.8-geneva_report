from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import NavRecord
from .forms import NavForm

# Get an instance of a logger
import logging
logger = logging.getLogger('app_nav')

# to make certain views exempt from security protection
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt	# CAUTION! this view is not protected by CSRF, any one can
				# change your site's data
def nav(request):
	logger.info('nav(): enter')
	if request.method == 'POST':
		logger.debug('nav(): POST')
		form = NavForm(request.POST)
		if form.is_valid():
			logger.debug('nav(): nav form valid: {0}, {1}, {2}'.format(
							form.cleaned_data['portfolio_id'], form.cleaned_data['date'], form.cleaned_data['nav']))
			n, created = NavRecord.objects.update_or_create(
							date=str(form.cleaned_data['date']), 
							portfolio_id=form.cleaned_data['portfolio_id'],
							defaults={'nav':form.cleaned_data['nav'], 
										'num_units':form.cleaned_data['num_units'], 
										'unit_price':form.cleaned_data['unit_price']}
						)
			if created:
				logger.debug('nav(): nav record created')
			else:
				logger.debug('nav(): nav record updated')

			return HttpResponse('OK')

		else:
			logger.error('nav(): nav form has invalid data: {0}'.format(form.errors))
			raise Http404('invalid form data')