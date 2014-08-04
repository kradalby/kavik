import base64
import uuid
from datetime import datetime


from django.shortcuts import render
from django.http import HttpResponse

from apps.consultants.models import Consultant

# Create your views here.

# Basic auth decorator for some security layer.
def basic_http_auth(f):
    def wrap(request, *args, **kwargs):
        if request.META.get('HTTP_AUTHORIZATION', False):
            authtype, auth = request.META['HTTP_AUTHORIZATION'].split(' ')
            auth = base64.b64decode(bytes(auth, 'utf-8'))
            # username, password = auth.split(':')
            # if username == 'test' and password == 'test':
            if auth == b'test:test':
                return f(request, *args, **kwargs)
            else:
                r = HttpResponse("Auth Required", status = 401)
                r['WWW-Authenticate'] = 'Basic realm="bat"'
                return r
        r = HttpResponse("Auth Required", status = 401)
        r['WWW-Authenticate'] = 'Basic realm="bat"'
        return r
        
    return wrap


@basic_http_auth
def maillist(request, team_id=None):
    if team_id.isnumeric():
        consultants = Consultant.objects.filter(team=team_id)
        text = generateMailList(consultants)
        return HttpResponse(text, content_type='text/plain')

    if team_id == "tl":
        consultants = Consultant.objects.filter(number__endswith='01')
        text = generateMailList(consultants)
        return HttpResponse(text, content_type='text/plain')


    consultants = Consultant.objects.all()
    text = generateMailList(consultants)
    return HttpResponse(text, content_type='text/plain')


@basic_http_auth
def vcf(request):
    consultants = Consultant.objects.all()
    vcf = "" 

    for c in consultants:
        uid = uuid.uuid5(uuid.NAMESPACE_DNS, c.number).__str__().upper()
        rev = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ') 
        vcf += """BEGIN:VCARD
VERSIOqN:3.0
N:%s;%s
FN:%s %s
ORG:%s
TITLE:%s
TEL;type=HOME;type=VOICE:%s
TEL;type=CELL;type=VOICE:%s
item1.ADR;type=HOME;type=pref:;;%s;%s;;%s;%s
EMAIL;TYPE=PREF,INTERNET:%s
REV:%s
UID:%s
END:VCARD
""" % ( c.lastName, c.firstName, c.firstName, c.lastName, "Klatrerosen", "TW Konsulent " + c.number, c.phone1, c.phone2, c.address, c.town, c.zipCode, c.country, c.email, rev, uid,)
    return HttpResponse(vcf, content_type='text/plain; charset=utf-8')




def generateMailList(consultants):
    text = ""

    for consultant in consultants:
        if consultant.email != " ":
            text += consultant.email + "\t" + consultant.firstName + " " + consultant.lastName + "\n"

    return text
        

