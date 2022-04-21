from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
import json
import os


default_packages = [
    {
        'name': 'django-axes',
        'install_cmd': 'pip install django-axes',
        'description': 'Axes is a Django plugin for keeping track of suspicious login attempts for your Django based website and implementing simple brute-force attack blocking.',
        'docs': 'https://django-axes.readthedocs.io/en/latest/index.html',
        'app': 'axes',
        'middleware': 'axes.middleware.AxesMiddleware',
        'auth_backend': 'axes.backends.AxesBackend',
        'settings_form': 'firebrick.ui.settings.forms.DjangoAxesSettingsForm',
        'credit': 'Jazzband',
        'credit_link': 'https://github.com/jazzband',
        'required': []
    },
    {
        'name': 'Django reCAPTCHA',
        'install_cmd': 'pip install django-recaptcha',
        'description': 'Django reCAPTCHA form field/widget integration app.',
        'docs': 'https://github.com/torchbox/django-recaptcha#readme',
        'app': 'captcha',
        'middleware': None,
        'auth_backend': None,
        'settings_form': 'firebrick.ui.settings.forms.DjangoreCAPTCHASettingsForm',
        'credit': 'Torchbox',
        'credit_link': 'https://github.com/torchbox',
        'required': []
    },
    {
        'name': 'Django Countries',
        'install_cmd': 'pip install django-countries',
        'description': 'A Django application that provides country choices for use with forms, flag icons static files, and a country field for models.',
        'docs': 'https://github.com/SmileyChris/django-countries#readme',
        'app': 'django_countries',
        'middleware': None,
        'auth_backend': None,
        'settings_form': 'firebrick.ui.settings.forms.DjangoCountriesSettingsForm',
        'credit': 'Chris Beaven',
        'credit_link': 'https://github.com/SmileyChris',
        'required': []
    },
    {
        'name': 'Silk',
        'install_cmd': 'pip install django-silk',
        'description': 'Silk is a live profiling and inspection tool for the Django framework. Silk intercepts and stores HTTP requests and database queries before presenting them in a user interface for further inspection.',
        'docs': 'https://github.com/jazzband/django-silk#readme',
        'app': 'silk',
        'middleware': 'silk.middleware.SilkyMiddleware',
        'auth_backend': None,
        'settings_form': 'firebrick.ui.settings.forms.SilkSettingsForm',
        'credit': 'Jazzband',
        'credit_link': 'https://github.com/jazzband',
        'required': []
    }
]


apps = {
    'base': {
        'name': 'base',
        'app_import_path': 'base.apps.BaseConfig',
        'template_name': 'base'
    },
    'accounts': {
        'name': 'accounts',
        'app_import_path': 'accounts.apps.AccountsConfig',
        'template_name': 'accounts'
    }
}


def print_verbose(text, verbose):
    if verbose > 0:
        print(text)


class Command(BaseCommand):
    help = 'Creates firebrick UI settings directory'
    
    def handle(self, *args, **options):
        # Creating `firebrick` dir in the project if its does not exist
        if not os.path.isdir(os.path.join(os.getcwd(), 'firebrick')):
            os.mkdir(os.path.join(os.getcwd(), 'firebrick'))
        # Create the `packages.json` file if it does not already exist
        # If it exists check it contains a valid dict
        if not os.path.isfile(os.path.join(os.getcwd(), 'firebrick', 'packages.json')):
            with open(os.path.join(os.getcwd(), 'firebrick', 'packages.json'), 'w') as f:
                json.dump({}, f, indent=4)
            # Adding all the default packages to the `packages.json` file
            for package in default_packages:
                call_command(
                    'addpackage',
                    f'--name={package["name"]}',
                    f'--install-cmd={package["install_cmd"]}',
                    f'--description={package["description"]}',
                    f'--docs={package["docs"]}',
                    f'--app={package["app"]}',
                    f'--middleware={package["middleware"]}',
                    f'--auth-backend={package["auth_backend"]}',
                    f'--settings-form={package["settings_form"]}',
                    f'--credit={package["credit"]}',
                    f'--credit-link={package["credit_link"]}',
                    f'--required={json.dumps(package["required"])}'
                )
        else:
            # Checking the `packages.json` file contains a list
            # Open the file using 'r+' because if the file does not contain a dict
            # we will have to write a dict to it
            with open(os.path.join(os.getcwd(), 'firebrick', 'packages.json'), 'r+') as f:
                try:
                    data = json.load(f)
                # If the file does not contain a valid dict it will throw this error
                except json.decoder.JSONDecodeError:
                    json.dump({}, f, indent=4)
        
        # Create the `apps.json` file if it does not exist already
        # If it exists check it contains a valid dict
        if not os.path.isfile(os.path.join(os.getcwd(), 'firebrick', 'apps.json')):
            with open(os.path.join(os.getcwd(), 'firebrick', 'apps.json'), 'w') as f:
                json.dump(apps, f, indent=4)
        else:
            # Checking the `packages.json` file contains a dict
            # Open the file using 'r+' because if the file does not contain a dict
            # we will have to write a dict to it
            with open(os.path.join(os.getcwd(), 'firebrick', 'apps.json'), 'r+') as f:
                try:
                    data = json.load(f)
                # If the file does not contain a valid dict it will throw this error
                except json.decoder.JSONDecodeError:
                    json.dump(apps, f, indent=4)
