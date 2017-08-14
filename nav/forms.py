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

	def clean_nav(self):
		nav = self.cleaned_data['nav']
		if nav <= 0:
			raise forms.ValidationError('nav {0} is negative'.format(nav))

		return nav

	def clean_portfolio_id(self):
		id = self.cleaned_data['portfolio_id']
		if re.search('[0-9]{5}', id) is None:	# id is a 5-digit string
			raise forms.ValidationError('portfolio_id {0} is not valid'.format(id))

		return id
