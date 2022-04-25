from django.core.management.templates import TemplateCommand
from django.core.management import call_command
from firebrick.management.click_commands.cli import cli
import subprocess
import requests
import click
import git
import os


@cli.command()
@click.argument('name', type=str, required=True)
def init(name):
        # Making a instance of the `TemplateCommand` class to use the `validate_name` function
        django_command_template = TemplateCommand()
        django_command_template.a_or_an = 'an'
        django_command_template.app_or_project = 'project'
        django_command_template.validate_name(name)
        
        # Asking the user if they want to create a git repo
        if click.confirm('Would you like to make a git repo?'):
            if click.confirm('Would you like to use a diffrent name for the repo?'):
                repo_name = click.prompt('Repo name')
            else:
                repo_name = name
            # Create repo
            git.Repo.init(repo_name)
            # Create README.md
            with open(os.path.join(repo_name, 'README.md'), 'w') as f:
                f.write(f'# {repo_name}')

            if click.confirm('Would you like to create a `.gitingnore` file'):
                # Get the python gitignore template
                r = requests.get('https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore')
                with open(os.path.join(repo_name, '.gitignore'), 'w') as f:
                    f.write(r.text)
            # Move to inside the repo dir so the django project is created inside of the repo
            os.chdir(os.path.join(os.getcwd(), repo_name))
                
        # Creating the django project
        call_command('startproject', name)
        
        # Need to add editing settings to add firebrick to installed_apps
        
        # Get the contents of `settings.py` so we can put it in `base.py`
        with open(os.path.join(name, name, 'settings.py'), 'r') as f:
            base_settings = f.read()
        
        # Deleting the `settings.py` file
        # So it can be replaced by the firebrick settings format
        os.remove(os.path.join(name, name, 'settings.py'))
        
        # Creating the firebrick settings format
        # I know I am not the first person to do settings this way but
        # Idk what else to call it
        settings_dir_path = os.path.join(name, name, 'settings')
        
        os.mkdir(settings_dir_path)
        
        # Creating a `__init__.py` file so that settings can be imported
        with open(os.path.join(settings_dir_path, '__init__.py'), 'w') as f:
            f.write('from .base import *\n')
        
        # Creating base django settings file
        with open(os.path.join(settings_dir_path, 'base.py'), 'w') as f:
            f.write(base_settings)
        
        # Asking the user if they want to create a virtual env
        virtualenv = click.prompt('What virtual environment would you like to use?', type=click.Choice(['None', 'pipenv']))
        
        if virtualenv == 'pipenv':
            subprocess.run('pipenv install django', shell=True)
            subprocess.run('pipenv install firebrick', shell=True)