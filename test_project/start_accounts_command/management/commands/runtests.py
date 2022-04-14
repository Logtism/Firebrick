from django.core.management.base import BaseCommand, CommandError
from firebrick.templates.templating import GenerateFromTemplate, TemplateFromFiles
from django.core.management import call_command
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