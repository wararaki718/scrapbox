from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'sample'

    def handle(self, *args, **kwards):
        self.stdout.write('hello, command!')
