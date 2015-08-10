
import uuid

from datetime import datetime

from apps.consultants.models import Consultant

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Outputs the teamleader email mail list for bash scripts'

    def handle(self, *args, **options):
        consultants = Consultant.objects.all()
        vcf = ''

        for c in consultants:
            uid = uuid.uuid5(uuid.NAMESPACE_DNS, c.number).__str__().upper()
            rev = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
            vcf += '''BEGIN:VCARD
VERSION:3.0
N:{};{}
FN:{} {}
ORG:{}
TITLE:{}
TEL;type=HOME;type=VOICE:{}
TEL;type=CELL;type=VOICE:{}
item1.ADR;type=HOME;type=pref:;;{};{};;{};{}
EMAIL;TYPE=PREF,INTERNET:{}
REV:{}
UID:{}
END:VCARD
'''.format(c.lastName, c.firstName, c.firstName, c.lastName, 'Klatrerosen', 'TW Konsulent ' + c.number, c.phone1, c.phone2, c.address, c.town, c.zipCode, c.country, c.email, rev, uid,)

        print(vcf)  # NOQA
