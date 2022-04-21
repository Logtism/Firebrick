from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
import subprocess
import firebrick
import argparse
import os



class Command(BaseCommand):
    help = 'Run the firebrick django UI'
    
    def add_arguments(self, parser):
        parser.add_argument('-p', '--port', type=int, default=9000)
    
    def handle(self, port, *args, **options):
        # Get the path of the firebrick settings dir in the project
        firebrick_settings_path = os.path.join(os.getcwd(), 'firebrick')
        # Check if a firebrick settings dir exists
        if not os.path.isdir(firebrick_settings_path):
            options['stdout'].write('Firebrick ui settings directory does not exist use command `python manage.py firebrick_init` to create firebrick ui settings.')
            # Return so the rest of the function does not execute
            return None
        # Moving to the correct dir to run the firebrick ui
        os.chdir(os.path.join(firebrick.__path__[0], 'ui'))
        # Running cmd in try except cause if not when pressing ctrl+c
        # Will cause a error and traceback for the kwyboard interrupt
        try:
            # Passing 'settings' to the commands
            # Because if not it will not pickup the correct settings file

            # Making migrations and migrating the database
            # Because some parts of the ui use models
            subprocess.run(f'python manage.py makemigrations -v=0 --settings=firebrick.ui.ui.settings', shell=True)
            subprocess.run(f'python manage.py migrate -v=0 --settings=firebrick.ui.ui.settings', shell=True)
            # Using `runuiserver` command so that the firebrick settings path can be passed
            subprocess.run(f'python manage.py runuiserver --port={port} --settings=firebrick.ui.ui.settings --firebrick-settings={firebrick_settings_path}', shell=True)
        except KeyboardInterrupt:
            pass