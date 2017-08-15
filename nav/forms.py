# All forms class for the Book app goes here.
from django import forms
import re



class NavForm(forms.Form):
	"""
	To submit NavRecord data.
	"""
	portfolio_id = forms.CharField(max_length=10)
	date = forms.DateField()
	nav = forms.FloatField()
	num_units = forms.FloatField()
	unit_price = forms.FloatField()

	def clean_nav(self):
		nav = self.cleaned_data['nav']
		if nav <= 0:
			raise forms.ValidationError('nav {0} is negative'.format(nav))

		return nav
	
	def clean_num_units(self):
		num_units = self.cleaned_data['num_units']
		if num_units <= 0:
			raise forms.ValidationError('num_units {0} is negative'.format(num_units))

		return num_units

	def clean_unit_price(self):
		unit_price = self.cleaned_data['unit_price']
		if unit_price <= 0:
			raise forms.ValidationError('unit_price {0} is negative'.format(unit_price))

		return unit_price
	
	def clean_portfolio_id(self):
		id = self.cleaned_data['portfolio_id']
		if re.search('[0-9]{5}', id) is None:	# id is a 5-digit string
			raise forms.ValidationError('portfolio_id {0} is not valid'.format(id))

		return id
