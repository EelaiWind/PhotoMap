from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.demo, name='demo'),
	url(r'^post/$', views.post, name='post'),
	url(r'^edit/$', views.editMarker, name='editMarker'),
]