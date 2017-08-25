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
from id_lookup.views import fbview, security_lookup
import geneva_report.views
import nav.views



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', geneva_report.views.hello),
    url(r'^json/$', fbview),
    url(r'^securities/$', security_lookup),

    url(r'^form-serial/$', geneva_report.views.form_serial),

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
	
	# GET:  
	# 	   /nav/19437/ytd/, nav record for 19437, year to date
	# 	   /nav/19437/mtd/, nav record for 19437, month to date
	# 	   /nav/19437/30/, nav record for 19437, for the last 30 days
	# 
	url(r'^nav/([0-9]{5})/([a-zA-Z]{3})/$', nav.views.nav_history),
	url(r'^nav/([0-9]{5})/(\d+)/$', nav.views.nav_history),
]



