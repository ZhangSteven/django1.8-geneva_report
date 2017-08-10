from django.db import models
import json

# Create your models here.
class Security(models.Model):
	"""
	Based on legacy security id used by custodian banks, find security id 
	used by Geneva and its currency.
	"""
	security_id_type = models.CharField(max_length=10)
	security_id = models.CharField(max_length=30)
	name = models.CharField(max_length=150)
	currency = models.CharField(max_length=10, blank=True)
	isin = models.CharField(max_length=30, blank=True)
	bloomberg_figi = models.CharField(max_length=30, blank=True)
	geneva_investment_id = models.CharField(max_length=50, blank=True)
	comments = models.CharField(max_length=150, blank=True)



	def to_json(self):
		"""
		Create a json object based on the security fields
		"""
		data = {
			'security_id_type':self.security_id_type,
			'security_id':self.security_id,
			'name':self.name,
			'currency':self.currency,
			'isin':self.isin,
			'bloomberg_figi':self.bloomberg_figi,
			'geneva_investment_id':self.geneva_investment_id,
			'comments':self.comments
		}
		return json.dumps(data)



	def __str__(self):
		return '_'.join([self.security_id_type, self.security_id, \
						self.name[0:min(20, len(self.name))]])