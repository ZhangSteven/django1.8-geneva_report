from django.contrib import admin

# Register your models here.
from .models import Portfolio, NavRecord

admin.site.register(Portfolio)
admin.site.register(NavRecord)