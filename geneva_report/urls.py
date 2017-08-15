"""geneva_report URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from .views import hello
from id_lookup.views import fbview, security_lookup
import nav.views



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^json/$', fbview),
    url(r'^securities/$', security_lookup),

	# GET: /nav/, latest nav record for all portfolios
	# POST: /nav/, update nav record for a portfolio
	url(r'^nav/$', nav.views.nav),	

	# GET: /nav/20170129/, nav records for all portfolios
	# 		as of certain date
	# 
	# 	   /nav/20170129-20170228/, nav records for all
	# 		portfolios between two dates
	# url(r'^nav/([0-9]{8})/$', nav.views.nav_by_date),
	# url(r'^nav/([0-9]{8}-[0-9]{8})/$', nav.views.nav_by_date),
	
	# GET: /nav/19437/, latest nav records for one portfolio
	# 
	# 	   /nav/19437/20170129/, nav record for one portfolio
	# 		as of certain date.
	# 
	#	   /nav/19437/20170129-20170228/, nav records for one
	# 		portfolio between two dates
	# url(r'^nav/$', nav.views.nav),
	# url(r'^nav/$', nav.views.nav),
]



