from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^donate/$', views.donate, name='donate'),
	url(r'^donate/charge/$', views.donate_charge, name='checkout_charge'),


]


