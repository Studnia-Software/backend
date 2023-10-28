from django.core.management.base import BaseCommand, CommandError
from  backendapp.models import Farm, User


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("siema eniu odbyt")
   