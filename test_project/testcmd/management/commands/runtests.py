from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
import firebrick
import subprocess
import shutil
import os


class Command(BaseCommand):
    help = 'Creates a firebrick accounts app in your django project.'
    
    def handle(self, *args, **options):
        call_command('test')
        
        call_command('startaccountsapp', '-t')
        
        call_command('test', 'accounts')
        
        if os.path.isdir(os.path.join(os.getcwd(), 'accounts')):
            shutil.rmtree(os.path.join(os.getcwd(), 'accounts'))
            
        os.chdir(os.path.join(firebrick.__path__[0], 'ui'))
        
        subprocess.run(f'python manage.py test --settings=firebrick.ui.ui.settings', shell=True)