from django.conf.urls import patterns, include, url

from users import views

urlpatterns = patterns('',
	# ex: /users/
	url(r'^$', views.index, name='index'),
	#url(r'^', include('django.contrib.auth.urls')),
	url(r'^login/', views.user_login, name='login'),
	url(r'^logout/', views.user_logout, name='logout'),
	url(r'^register/', views.register, name='register'),
	url(r'^profile/', views.profile, name='profile'),
	url(r'^groupsession/', views.group_session, name='groupsession')
	url(r'^lfconnect/', views.lfconnect, name='lfconnect')
) 