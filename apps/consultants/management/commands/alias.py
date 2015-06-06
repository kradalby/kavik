from django.core.management.base import BaseCommand, CommandError
from apps.consultants.models import Consultant
from kavik.settings import BASE_DIR
import os

class Command(BaseCommand):
    help = "Outputs the teamleader email mail list"


    def handle(self, *args, **options):
        consultants = Consultant.objects.all()
        text = ""

        if args[0] == "sympa":
            for consultant in consultants:
                if consultant.email != " ":
                    text += consultant.email + "\t" + consultant.firstName + " " + consultant.lastName + "\n"
        elif args[0] == "alias":
            text = "konsulenter: "
            for consultant in consultants:
                if consultant.email != " ":
                    text += consultant.email + " "
        else:
            text = "Not available"
        print(text)

