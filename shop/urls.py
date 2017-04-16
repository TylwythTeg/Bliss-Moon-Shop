from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^charge/$', views.charge, name='charge'),
	url(r'^checkout/$', views.checkout, name='checkout'),
	url(r'^checkout/charge/$', views.checkout_charge, name='checkout_charge'),


]


