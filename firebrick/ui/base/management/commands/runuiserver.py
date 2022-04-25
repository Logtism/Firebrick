from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from firebrick.ui.ui import firebrick_settings
import subprocess
import argparse
import firebrick
import json
import os


def load_firebrick_ui_settings(path):
    with open(os.path.join(path, 'packages.json'), 'r') as f:
        firebrick_settings['packages'] = json.load(f)
    # Gathering installed and not installed packages
    firebrick_settings['installed_packages'] = {}
    firebrick_settings['not_installed_packages'] = {}
    for package in firebrick_settings['packages']:
        if firebrick_settings['packages'][package]['enabled']:
            firebrick_settings['installed_packages'][package] = firebrick_settings['packages'][package]
        else:
            firebrick_settings['not_installed_packages'][package] = firebrick_settings['packages'][package]
    with open(os.path.join(path, 'apps.json'), 'r') as f:
        firebrick_settings['apps'] = json.load(f)
    # Gathering installed and not installed apps
    firebrick_settings['installed_apps'] = {}
    firebrick_settings['not_installed_apps'] = {}
    for app in firebrick_settings['apps']:
        if firebrick_settings['apps'][app]['enabled']:
            firebrick_settings['installed_apps'][app] = firebrick_settings['apps'][app]
        else:
            firebrick_settings['not_installed_apps'][app] = firebrick_settings['apps'][app]


class Command(BaseCommand):
    help = 'Run the firebrick django ui'
    
    def add_arguments(self, parser):
        parser.add_argument('-p', '--port', type=int)
        parser.add_argument('-f', '--firebrick-settings-path', type=str)
    
    def handle(self, port, firebrick_settings_path, *args, **options):
        load_firebrick_ui_settings(firebrick_settings_path)
        
        call_command('runserver', port, settings='firebrick.ui.ui.settings')