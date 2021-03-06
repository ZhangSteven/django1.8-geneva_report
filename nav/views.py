from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import NavRecord
from .forms import NavForm
from .view_handler import get_latest_navrecords, get_history_navrecords, \
							portfolio_exists, get_portfolio_name
from datetime import date, timedelta

# Get an instance of a logger
import logging
logger = logging.getLogger(__name__)

# to make certain views exempt from security protection
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt	# CAUTION! this view is not protected by CSRF, any one can
				# change your site's data
def nav(request):
	logger.info('nav(): enter, method={0}'.format(request.method))
	if request.method == 'POST':
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

	elif request.method == 'GET':
		result = get_latest_navrecords()
		return render(request, 'latest.html', {'result':result})



def nav_history(request, portfolio_id, history):
	logger.info('nav_history(): portfolio_id={0}, history={1}'.format(portfolio_id, history))
	if not portfolio_exists(portfolio_id):
		return render(request, 'error.html', 
						{'error_message':'Sorry, portfolio {0} does not exist.'.format(portfolio_id)}) 

	if history in ['ytd', 'mtd']:
		if history == 'ytd':
			date1 = date(date.today().year, 1, 1)
		else:
			date1 = date(date.today().year, date.today().month, 1)
		
	else:
		try:
			history = int(history)
			date1 = date.today() - timedelta(days=history)
		except:
			logger.error('nav_history(): history {0} is not a valid indicator'.format(history))
			return render(request, 'error.html', 
							{'error_message': 'Sorry, {0} is not a valid request'.format(request.get_full_path())})

	result = get_history_navrecords(portfolio_id, date1, date.today())
	return render(request, 'holding.html', {'portfolio':get_portfolio_name(portfolio_id), 
											'result':result})