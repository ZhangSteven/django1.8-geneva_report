# coding=utf-8
# 
# Here we put all functions that will be called from within the views.
from .models import Portfolio, NavRecord
from django.core.exceptions import ObjectDoesNotExist
from datetime import date, timedelta


# Get an instance of a logger
import logging
logger = logging.getLogger(__name__)



def get_latest_navrecords():
	"""
	Get the latest nav record for each portfolio defined in the Portfolio
	table.

	Return a list of NavRecord objects.
	"""
	logger.info('get_latest_navrecords(): enter')
	result = []
	for p in Portfolio.objects.all():

		# for each portfolio id, we extract all nav records within 14 days
		# from today. This is to save sorting time.
		# 
		# Here we assume that all portfolio's latest nav records will be 
		# within 14 days from today.
		logger.debug('get_latest_navrecords(): portfolio id {0}'.format(p.portfolio_id))
		nav_records = NavRecord.objects.filter(portfolio_id=p.portfolio_id,
												date__gt=date.today()-timedelta(days=14))
		if len(nav_records) > 0:
			logger.debug('get_latest_navrecords(): get {0} result for portfolio id {1}'.
							format(len(nav_records), p.portfolio_id))
			result.append(nav_records.order_by('-date')[0])

	return result



def get_history_navrecords(portfolio_id, date1, date2):
	"""
	Get a list of NavRecord objects whose date is in between date1 and date2, inclusive.

	The objects are sorted by date, earlier dates come first.
	"""
	logger.info('get_history_navrecords(): enter: portfolio_id={2}, date1={0}, date2={1}'
					.format(date1, date2, portfolio_id))
	nav_records = NavRecord.objects.filter(portfolio_id=portfolio_id,
												date__gte=date1, date__lte=date2)
	logger.debug('get {0} results'.format(len(nav_records)))
	return nav_records.order_by('date')



def portfolio_exists(portfolio_id):
	try:
		Portfolio.objects.get(portfolio_id=portfolio_id)
	except ObjectDoesNotExist:
		return False

	return True