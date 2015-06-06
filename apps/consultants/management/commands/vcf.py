from django.core.management.base import BaseCommand, CommandError
from apps.consultants.models import Consultant
from kavik.settings import BASE_DIR
import os
import uuid
from datetime import datetime

class Command(BaseCommand):
    help = "Outputs the teamleader email mail list for bash scripts"


    def handle(self, *args, **options):
        consultants = Consultant.objects.all()
        vcf = "" 
    
        for c in consultants:
            uid = uuid.uuid5(uuid.NAMESPACE_DNS, c.number).__str__().upper()
            rev = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ') 
            vcf += """BEGIN:VCARD
VERSION:3.0
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
    
        print(vcf)
