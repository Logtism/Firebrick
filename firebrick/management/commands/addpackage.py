from django.core.management.base import BaseCommand, CommandError
import json
import os


class Command(BaseCommand):
    help = 'Adds a package to the firebrick ui settings packages.json'

    def add_arguments(self, parser):
        parser.add_argument('--name', type=str, required=True)
        parser.add_argument('--install-cmd', type=str, required=True)
        parser.add_argument('--description', type=str, required=True)
        parser.add_argument('--docs', type=str)
        parser.add_argument('--app', type=str, default=None)
        parser.add_argument('--middleware', type=str, default=None)
        parser.add_argument('--auth-backend', type=str, default=None)
        parser.add_argument('--settings-form', type=str, default=None)
        parser.add_argument('--credit', type=str, default=None)
        parser.add_argument('--credit-link', type=str, default=None)
        parser.add_argument('--required', type=str, default='[]')
        parser.add_argument('--path', type=str, default=os.path.join(os.getcwd(), 'firebrick', 'packages.json'))
    
    def handle(
            self,
            name,
            install_cmd,
            description,
            docs,
            app,
            middleware,
            auth_backend,
            settings_form,
            credit,
            credit_link,
            required,
            path,
            *args,
            **options
        ):
        # Check if a firebrick settings dir exists
        if not os.path.isdir(os.path.join(os.getcwd(), 'firebrick')):
            self.stdout.write('Firebrick ui settings directory does not exist use command `python manage.py firebrick_init` to create firebrick ui settings.')
            # Return so the rest of the function does not execute
            return None
        with open(path, 'r') as f:
            data = json.load(f)
        data[name] = {
                'name': name,
                'install_cmd': install_cmd,
                'description': description,
                'docs': None if docs == 'None' else docs,
                'app': None if app == 'None' else app,
                'middleware': None if middleware == 'None' else middleware,
                'auth_backend': None if auth_backend == 'None' else auth_backend,
                'settings_form': None if settings_form == 'None' else settings_form,
                'credit': None if credit == 'None' else credit,
                'credit_link': None if credit_link == 'None' else credit_link,
                'required': json.loads(required),
                'enabled': False
            }
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)