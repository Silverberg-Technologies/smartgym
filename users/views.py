from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import views

from django.views.decorators.cache import never_cache

from users.models import Groupsession
import requests

# Create your views here.

def index(request):
	return render(request, 'users/index.html')

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect(reverse('users:index'))
	else:
		form = UserCreationForm()
	return render(request, 'registration/register.html', {'form' : form, })

def user_login(request):
	template_response = views.login(request)
	return template_response

def user_logout(request):
	template_response = views.logout(request)
	return template_response

@never_cache
def profile(request):
	if request.method == 'POST':
		new_first_name = request.POST.get("firstname",'')
		new_last_name = request.POST.get("lastname", '')
		new_email = request.POST.get("email", '')

		user = get_object_or_404(User, username=request.user.get_username())
		user.first_name = new_first_name
		user.last_name = new_last_name
		user.email = new_email
		user.save()
		
	if request.method == 'GET':
		code = request.GET.get('code')
		if(code):
			redirect_uri = "http://46.101.58.27:9000/users/lfconnect/" + request.user.get_username() + "/"
			response_data = { "grant_type":"authorization_code", 
							"client_id":"6299bd2d816f49a890ee481beb22c07d",
							"client_secret":"1a4e3fb91f88d9f4d759f7cb3542d138",
							"code":code,
							"redirect_uri":"http://46.101.58.27:9000/users/lfconnect"}
			r = requests.post("https://vtqa.lfconnect.com/web/authorizeresponse", response_data)				
	return render(request, 'users/profile.html')

def lfconnect(request):
	print(request.GET.get('access_token')
	if request.method == 'GET':
		access_token = request.GET.get('access_token')
		refresh_token = request.GET.get('refresh_token')
		expires_in = request.GET.get('expires_in')
		print(access_token)
		print(expires_in)
		print(request.user.get_username())
		# user = get_object_or_404(User, username=request.user.get_username())


def group_session(request):
	if request.method == 'POST':
		button_id = request.POST.get("button")
		[session_id, attending] = button_id.split(".")
		session = get_object_or_404(Groupsession, id=session_id)
		print("List of users attending")
		print(session.users_attending.all())
		print(attending)
		if attending == "0":
			session.users_attending.remove(request.user)
			print("Removing user from session")
			print("List of users attending")
			print(session.users_attending.all())
		else:
			session.users_attending.add(request.user)
			print("Adding user to session")
			print("List of users attending")
			print(session.users_attending.all())
	group_sessions = Groupsession.objects.all()
	return render(request, 'users/groupsession.html', {'group_sessions' : group_sessions})