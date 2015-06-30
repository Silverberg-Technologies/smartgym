from django.contrib.auth.models import User
from users.models import Oauth2Codes

def is_lf_connected(username):
    try:
        user = User.objects.get(username=username)
        try:
            oauth = Oauth2Codes.objects.get(user=user)
            return True
        except Oauth2Codes.DoesNotExist:
            return False
    except User.DoesNotExist:
        return False

