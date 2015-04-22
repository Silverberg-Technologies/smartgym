from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import views

from django.views.decorators.cache import never_cache
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
			
	return render(request, 'users/profile.html')