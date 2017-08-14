from django.db import models

# Create your models here.
class Portfolio(models.Model):
	portfolio_id = models.CharField(primary_key=True, max_length=10)
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name



class NavRecord(models.Model):
	date = models.DateField()
	portfolio = models.ForeignKey(Portfolio)
	nav = models.FloatField()

	def __str__(self):
		return ' '.join([self.portfolio.portfolio_id, str(self.date), str(self.nav)])