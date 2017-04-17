from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^charge/$', views.charge, name='charge'),
	url(r'^donate/$', views.donate, name='donate'),
	url(r'^donate/charge/$', views.donate_charge, name='checkout_charge'),


]


