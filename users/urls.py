from django.conf.urls import patterns, include, url

from users import views

urlpatterns = patterns('',
	# ex: /users/
	url(r'^$', views.index, name='index'),
	url(r'^', include('django.contrib.auth.urls')),
	url(r'^register/', views.register, name='register'),
)