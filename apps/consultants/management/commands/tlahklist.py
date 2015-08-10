from django.core.management.base import BaseCommand, CommandError
from apps.consultants.models import Consultant
from kavik.settings import BASE_DIR
import os

class Command(BaseCommand):
    help = 'Outputs the teamleader numbers formated as ahk list'


    def handle(self, *args, **options):
        tl = Consultant.objects.filter(number__endswith='01', active=True)
        string = 'Teams = '
        for t in tl:
            string += t.number[:2] + ','
        print(string[:-1])
        
