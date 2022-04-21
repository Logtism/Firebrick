from django.core.management.base import BaseCommand, CommandError
import argparse
import firebrick
import os
import subprocess


class Command(BaseCommand):
    help = 'Run the firebrick django ui'
    
    def add_arguments(self, parser):
        parser.add_argument('-p', '--port', type=int)
        parser.add_argument('-f', '--firebrick-settings', type=str)
    
    def handle(self, port, firebrick_settings, *args, **options):
        print(firebrick_settings)