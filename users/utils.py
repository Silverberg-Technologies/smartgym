from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from users.models import Oauth2Codes

def is_lf_connected(username):
    user = get_object_or_404(User, username=username)
    oauth = get_object_or_404(Oauth2Codes, user=user)
    return True if oauth else False
    #try:
    #    user = get_object_or_404(User, username=username)
    #    try:
    #        oauth = Oauth2Codes.objects.get(user=user)
    #        return True
    #    except Oauth2Codes.DoesNotExist:
    #        return False
    #except User.DoesNotExist:
    #    return False

