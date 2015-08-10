from apps.consultants.models import Consultant

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Outputs the teamleader email mail list'

    def handle(self, *args, **options):
        consultants = Consultant.objects.filter(active=True)
        text = ''

        if args[0] == 'sympa':
            for consultant in consultants:
                if consultant.email != ' ':
                    text += consultant.email + '\t' + consultant.firstName + ' ' + consultant.lastName + '\n'
        elif args[0] == 'alias':
            text = 'konsulenter: '
            for consultant in consultants:
                if consultant.email != ' ':
                    text += consultant.email + ' '
        elif args[0] == 'mailpimp':
            text = 'konsulenter@lists.klatrerosen.no:kristine@klatrerosen.no:'
            for consultant in consultants:
                if consultant.email != ' ':
                    text += consultant.email + ' '
        else:
            text = 'Not available'
        print(text)  # NOQA
