""" Various utility functions for the users module """

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from users.models import Oauth2Codes

from datetime import datetime, timedelta
import xml.etree.ElementTree as xmltree
import pytz
import requests

def is_lf_connected(username):
    """ 
    Checks if the account linked to a certain 
    username is connected to LFConnect.
    Returns a tuple of a success flag and
    a valid access token for that account.
    """
    user = get_object_or_404(User, username=username)
    try:
        oauth = Oauth2Codes.objects.get(user=user)
        access_token = get_valid_access_token(username, oauth)
        return (True, access_token)
    except Oauth2Codes.DoesNotExist:
        return (False, None)

def get_lf_data(access_token):
    """
    Get data from LFConnect that is associated
    with a certain access token.
    Returns a dictionary with the fields from the 
    LFUserProfile model, if LF connection is successful.
    """
    payload = {"access_token": access_token}
    r = requests.get("https://vtqa.lfconnect.com/web/api2/user", params=payload)
    xmlstr = r.content.decode('utf-8')
    if 'LFUser' in xmlstr:
        root = xmltree.fromstring(xmlstr)
        lfmodel = {}
        for child in root:
           lfmodel[child.tag] = child.text
        return lfmodel
    else:
        return None



def get_valid_access_token(username, oauth):
    """
    Uses the supplied oauth instance to
    fetch an access token. If it is expired,
    a new one is requested from LFConnect.
    """
    expire_time = oauth.expire_time
    is_valid = datetime.now(pytz.utc) - expire_time < timedelta(seconds=0)
    if is_valid:
        return oauth.access_token
    else:
        redirect_uri = "http://46.101.58.27:9000/users/accesstoken/" + str(username)
        request_data = { "grant_type": "refresh_token",
                         "client_id": "6299bd2d816f49a890ee481beb22c07d",
                         "client_secret": "1a4e3fb91f88d9f4d759f7cb3542d138",
                         "refresh_token": oauth.refresh_token,
                         "redirect_uri": redirect_uri
                       }
        response = requests.post("https://vtqa.lfconnect.com/web/refreshaccess", request_data)
    return oauth.access_token




