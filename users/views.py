from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.core.urlresolvers import reverse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import views, authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.views.decorators.cache import never_cache

from users.models import Groupsession, Oauth2Codes, LFUserProfile
from users.utils import is_lf_connected
from datetime import datetime, timedelta
import requests, pytz

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
    logout(request)
    username = ''
    password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active: # Inactive account == deleted account
                login(request, user)
                return HttpResponseRedirect(reverse('users:profile'))
    return render(request, 'registration/login.html')

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
                              "redirect_uri":redirect_uri}
            r = requests.post("https://vtqa.lfconnect.com/web/authorizeresponse", response_data)

    lf_connected, access_token = is_lf_connected(request.user)


    return render(request, 'users/profile.html', {'lf_connected': lf_connected})

def home(request):
    return render(request, 'users/home.html')

def lfconnect(request, username):
    if request.method == 'GET':
        access_token = request.GET.get('access_token')
        refresh_token = request.GET.get('refresh_token')
        expires_in = request.GET.get('expires_in')
        expire_time = datetime.now(pytz.utc) + timedelta(seconds=int(expires_in))
        user = get_object_or_404(User, username=username)
        o2c = Oauth2Codes(user=user,
                          access_token=access_token,
                          refresh_token=refresh_token,
                          expire_time=expire_time)
        o2c.save()


def get_lf_data(request):
    user = get_object_or_404(User, username=request.user)
    oauth = get_object_or_404(Oauth2Codes, user=user)
    access_token = oauth.access_token
    payload = {'access_token': access_token}
    r = requests.get("https://vtqa.lfconnect.com/web/api2/user", params=payload)
    if r.status_code is 200:
        print(r.content)
        return HttpResponse(r.content)
    else:
        print(r.content)
        return HttpResponse('User data not found')

def access_token_refresh(request):
    print("Token refresh")
    print("User is authenticated: %s" % request.user.is_authenticated())
    if request.method == 'GET' and request.user.is_authenticated():
        print('Trying to refresh token for user %s' % request.user)
        access_token = request.GET.get('access_token')
        refresh_token = request.GET.get('refresh_token')
        expires_in = request.GET.get('expires_in')
        expire_time = datetime.now(pytz.utc) + timedelta(seconds=int(expires_in))
        user = get_object_or_404(User, username=request.user)
        print('User fetch successful')
        o2c = Oauth2Codes.objects.get(user=user)
        o2c.access_token=access_token
        o2c.refresh_token=refresh_token
        o2c.expire_time=expire_time
        o2c.save()
        print('Token should have been refreshed')
        return HttpResponse(status=200)
    return HttpResponseNotFound()

#def displaydata(request, data):
#    return HttpResponse(data)


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
