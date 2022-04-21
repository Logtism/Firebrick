from django.test import TestCase
from django.core.management import call_command
import shutil
import json
import os
from io import StringIO
from firebrick.management.commands.init_firebrick import apps


class TestInit_FirebrickCommand(TestCase):
    def tearDown(self):
        if os.path.isdir(os.path.join(os.getcwd(), 'firebrick')):
            shutil.rmtree(os.path.join(os.getcwd(), 'firebrick'))
            
    def test_create_from_scratch(self):
        # Run the command
        call_command('init_firebrick')
        # Check that the correct files/dirs were created
        self.assertTrue(os.path.isdir(os.path.join(os.getcwd(), 'firebrick')))
        self.assertTrue(os.path.isfile(os.path.join(os.getcwd(), 'firebrick', 'packages.json')))
        with open(os.path.join(os.getcwd(), 'firebrick', 'packages.json'), 'r') as f:
            self.assertEquals(type(json.load(f)), dict)
        self.assertTrue(os.path.isfile(os.path.join(os.getcwd(), 'firebrick', 'apps.json')))
        with open(os.path.join(os.getcwd(), 'firebrick', 'apps.json'), 'r') as f:
            self.assertEquals(json.load(f), apps)
            
    def test_create_file_with_dir_already_created(self):
        # Create dir `firebrick`
        os.mkdir(os.path.join(os.getcwd(), 'firebrick'))
        # Run the command
        call_command('init_firebrick')
        # Check that files were created
        self.assertTrue(os.path.isfile(os.path.join(os.getcwd(), 'firebrick', 'packages.json')))
        with open(os.path.join(os.getcwd(), 'firebrick', 'packages.json'), 'r') as f:
            self.assertEquals(type(json.load(f)), dict)
        self.assertTrue(os.path.isfile(os.path.join(os.getcwd(), 'firebrick', 'apps.json')))
        with open(os.path.join(os.getcwd(), 'firebrick', 'apps.json'), 'r') as f:
            self.assertEquals(json.load(f), apps)
    
    def test_create_dict_inside_already_created_files(self):
        # Create dir `firebrick`
        os.mkdir(os.path.join(os.getcwd(), 'firebrick'))
        # Create `package.json` and `apps.json`
        with open(os.path.join(os.getcwd(), 'firebrick', 'packages.json'), 'w') as f:
            pass
        with open(os.path.join(os.getcwd(), 'firebrick', 'apps.json'), 'w') as f:
            pass
        # Run the command
        call_command('init_firebrick')
        # Check the files were fixed
        with open(os.path.join(os.getcwd(), 'firebrick', 'packages.json'), 'r') as f:
            self.assertEquals(type(json.load(f)), dict)
        with open(os.path.join(os.getcwd(), 'firebrick', 'apps.json'), 'r') as f:
            self.assertEquals(json.load(f), apps)
            

class TestAddPackageCommand(TestCase):
    name = 'test_package'
    install_cmd = 'pip install test_package'
    description = 'this is a test package'
    docs = 'docs_link'
    app = 'test_package.app'
    middleware = 'test_package.middleware'
    auth_backend = 'test_package.auth_backend'
    settings_form = 'test_package.settings_form'
    credit = 'testing'
    credit_link = 'testing_link'
    required = ['other_test_package']
    
    def tearDown(self):
        if os.path.isdir(os.path.join(os.getcwd(), 'firebrick')):
            shutil.rmtree(os.path.join(os.getcwd(), 'firebrick'))
            
    def test_no_firebrick_ui_settings(self):
        # Run the command and get the output
        out = StringIO()
        call_command(
            'addpackage',
            name=self.name,
            install_cmd=self.install_cmd,
            description=self.description,
            
            stdout=out
        )
        # Check that the command outputs the help msg
        self.assertEquals('Firebrick ui settings directory does not exist use command `python manage.py firebrick_init` to create firebrick ui settings.', out.getvalue())
    
    def test_only_required_arguments(self):
        # Run the `init_firebrick` to create firebrick ui settings files
        call_command('init_firebrick')
        # Run the command and get the output
        out = StringIO()
        call_command(
            'addpackage',
            name=self.name,
            install_cmd=self.install_cmd,
            description=self.description,
            
            stdout=out
        )
        # Assert that the command does not output anything
        self.assertEquals('', out.getvalue())
        
        with open(os.path.join(os.getcwd(), 'firebrick', 'packages.json'), 'r') as f:
            data = json.load(f)
        
        # Checking the `test_package` key is in the `packages.json` file
        self.assertIn('test_package', data)
        # Checking that the file contains the correct data on the package
        test_package = data['test_package']
        self.assertEquals(test_package['name'], self.name)
        self.assertEquals(test_package['install_cmd'], self.install_cmd)
        self.assertEquals(test_package['description'], self.description)
        self.assertEquals(test_package['docs'], None)
        self.assertEquals(test_package['app'], None)
        self.assertEquals(test_package['middleware'], None)
        self.assertEquals(test_package['auth_backend'], None)
        self.assertEquals(test_package['settings_form'], None)
        self.assertEquals(test_package['credit'], None)
        self.assertEquals(test_package['credit_link'], None)
        self.assertEquals(test_package['required'], [])
        self.assertEquals(test_package['enabled'], False)
        
    def test_all_arguments(self):
        # Run the `init_firebrick` to create firebrick ui settings files
        call_command('init_firebrick')
        # Run the command and get the output
        out = StringIO()
        call_command(
            'addpackage',
            name=self.name,
            install_cmd=self.install_cmd,
            description=self.description,
            docs=self.docs,
            app=self.app,
            middleware=self.middleware,
            auth_backend=self.auth_backend,
            settings_form=self.settings_form,
            credit=self.credit,
            credit_link=self.credit_link,
            required=json.dumps(self.required),
            
            stdout=out
        )
        # Assert that the command does not output anything
        self.assertEquals('', out.getvalue())
        
        with open(os.path.join(os.getcwd(), 'firebrick', 'packages.json'), 'r') as f:
            data = json.load(f)
        
        # Checking the `test_package` key is in the `packages.json` file
        self.assertIn('test_package', data)
        # Checking that the file contains the correct data on the package
        test_package = data['test_package']
        self.assertEquals(test_package['name'], self.name)
        self.assertEquals(test_package['install_cmd'], self.install_cmd)
        self.assertEquals(test_package['description'], self.description)
        self.assertEquals(test_package['docs'], self.docs)
        self.assertEquals(test_package['app'], self.app)
        self.assertEquals(test_package['middleware'], self.middleware)
        self.assertEquals(test_package['auth_backend'], self.auth_backend)
        self.assertEquals(test_package['settings_form'], self.settings_form)
        self.assertEquals(test_package['credit'], self.credit)
        self.assertEquals(test_package['credit_link'], self.credit_link)
        self.assertEquals(test_package['required'], self.required)
        self.assertEquals(test_package['enabled'], False)


class TestUICommand(TestCase):
    def tearDown(self):
        if os.path.isdir(os.path.join(os.getcwd(), 'firebrick')):
            shutil.rmtree(os.path.join(os.getcwd(), 'firebrick'))
            
    def test_no_firebrick_ui_settings(self):
        # Run the command and get the output
        out = StringIO()
        call_command('ui', stdout=out)
        
        self.assertEquals('Firebrick ui settings directory does not exist use command `python manage.py firebrick_init` to create firebrick ui settings.', out.getvalue())
    
    # There could be more tests but I don't know how to test if the command runs the `runserver` command.
    # Please make a pull request or contact me on how to test this thank you.