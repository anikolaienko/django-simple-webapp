from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = "Generates hash from text password"

    def add_arguments(self, parser):
        parser.add_argument('passwords', nargs="+", type=str)

    def handle(self, *args, **options):
        for pw in options['passwords']:
            self.stdout.write(make_password(pw))
