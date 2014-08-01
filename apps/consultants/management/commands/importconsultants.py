from django.core.management.base import BaseCommand, CommandError
from apps.consultants.models import Consultant
from kavik.settings import BASE_DIR
import os

class Command(BaseCommand):
    help = "Imports tupos forhandlerlist into the database"

    def add_arguments(self, parser):
        parser.add_argument('conslist', required=True)


    def handle(self, *args, **options):
        if len(args) != 1:
            raise CommandError("This command takes only one argument")

        try:
            #file = open(os.path.join(BASE_DIR, args[0]), 'r').read()
            file = open(args[0], 'r').read()
            consultants = [x.split(',') for x in file.split('\n')]
            consultants.pop(-1)

            # Find the consultants that have been removed.
            unique_tupo = [x[0] for x in consultants]
            unique_django = [x.longUniqueTWNumber for x in Consultant.objects.all()]
            not_active = [x for x in unique_django if x not in unique_tupo]
          
           
            for c in consultants:
                c = [x.strip('"') for x in c]
                # print(c[8])
                cons = Consultant.objects.update_or_create(longUniqueTWNumber=c[0], defaults={
                    "longUniqueTWNumber" :  c[0], 
                    "ship"               :  c[1],
                    "team"               :  c[2],
                    "number"             :  c[3],
                    "position"           :  c[4],
                    "y"                  :  c[5],
                    "firstName"          :  c[6],
                    "lastName"           :  c[7],
                    "address"            :  c[8],
                    "zipCode"            :  c[9],
                    "town"               :  c[10],
                    "country"            :  c[11],
                    "phone1"             :  c[12],
                    "phone2"             :  c[13],
                    "email"              :  c[14],
                    "password"           :  c[15],
                    "y2"                 :  c[16],
                    "active"             :  True,
                })
                # cons.save()
            
            # Set removed consultants to unactive

            for c in not_active:
                cons = Consultant.objects.get(longUniqueTWNumber=c)
                cons.active = False
                cons.save()


        except Exception as e:
            print(e)
        
