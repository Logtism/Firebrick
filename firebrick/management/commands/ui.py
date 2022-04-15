from django.core.management.base import BaseCommand, CommandError
import argparse
import firebrick
import os
import subprocess


class Command(BaseCommand):
    help = 'Run the firebrick django ui'
    
    def add_arguments(self, parser):
        parser.add_argument('-p', '--port', type=int, default=9000)
    
    def handle(self, port, *args, **options):
        # Moving to the correct dir to run the project
        os.chdir(os.path.join(firebrick.__path__[0], 'ui'))
        # Running cmd in try except cause if not when pressing ctrl+c
        # Will cause a error and traceback
        try:
            subprocess.run(f'python manage.py makemigrations -v=0 --settings=firebrick.ui.ui.settings', shell=True)
            subprocess.run(f'python manage.py migrate -v=0 --settings=firebrick.ui.ui.settings', shell=True)
            # Passing 'settings' to the runserver cmd
            # because if not it will not pickup the correct settings file
            subprocess.run(f'python manage.py runserver {port} --settings=firebrick.ui.ui.settings', shell=True)
        except KeyboardInterrupt:
            pass