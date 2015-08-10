from django.core.management.base import BaseCommand, CommandError
from apps.consultants.models import Consultant
from kavik.settings import BASE_DIR
import os

class Command(BaseCommand):
    help = 'Outputs the teamleader email mail list for bash scripts'


    def handle(self, *args, **options):
        tl = Consultant.objects.filter(number__endswith='01', active=True)
        string = '#!/bin/bash\n'
        teams = 'teams=''
        for t in tl:
            string += 'epost[%s]=%s\n' % (t.number[:2], t.email)
            teams += '%s ' % t.number[:2]
        print(string)
        print(teams + ''')
        
