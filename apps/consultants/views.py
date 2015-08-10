import base64
import uuid
from datetime import datetime


from django.shortcuts import render
from django.http import HttpResponse

from apps.consultants.models import Consultant

from kavik.settings import BASIC_USER, BASIC_PASS

# Create your views here.

# Basic auth decorator for some security layer.
def basic_http_auth(f):
    def wrap(request, *args, **kwargs):
        if request.META.get('HTTP_AUTHORIZATION', False):
            authtype, auth = request.META['HTTP_AUTHORIZATION'].split(' ')
            auth = base64.b64decode(bytes(auth, 'utf-8'))
            # username, password = auth.split(':')
            # if username == 'test' and password == 'test':
            a = '%s:%s' % (BASIC_USER, BASIC_PASS)
            if auth == bytes(a, 'utf-8'):
                return f(request, *args, **kwargs)
            else:
                r = HttpResponse('Auth Required', status = 401)
                r['WWW-Authenticate'] = 'Basic realm='bat''
                return r
        r = HttpResponse('Auth Required', status = 401)
        r['WWW-Authenticate'] = 'Basic realm='bat''
        return r
        
    return wrap


@basic_http_auth
def maillist(request, team_id=None):
    if team_id and team_id.isnumeric():
        consultants = Consultant.objects.filter(team=team_id, active=True)
        text = generateMailList(consultants)
        return HttpResponse(text, content_type='text/plain')

    if team_id == 'tl':
        consultants = Consultant.objects.filter(number__endswith='01', active=True)
        text = generateMailList(consultants)
        return HttpResponse(text, content_type='text/plain')


    consultants = Consultant.objects.filter(active=True)
    text = generateMailList(consultants)
    return HttpResponse(text, content_type='text/plain')


@basic_http_auth
def vcf(request):
    pass




def generateMailList(consultants):
    pass
        

