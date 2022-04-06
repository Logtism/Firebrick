from django.test import TestCase, Client
from django.core.management import call_command
from django.conf import settings
import shutil
import os


class TestStartAccountsAppCommand(TestCase):
    def tearDown(self):
        if os.path.isdir(os.path.join(os.getcwd(), 'accounts')):
            shutil.rmtree(os.path.join(os.getcwd(), 'accounts'))
        
    def test_generate_accounts_app_without_templates(self):
        call_command('startaccountsapp')
        
        self.assertTrue(os.path.isdir(os.path.join(os.getcwd(), 'accounts')))
        self.assertFalse(os.path.isdir(os.path.join(os.getcwd(), 'accounts', 'templates')))
        
    def test_generate_accounts_app_with_templates_with_dash_t(self):
        call_command('startaccountsapp', '-t')
        
        self.assertTrue(os.path.isdir(os.path.join(os.getcwd(), 'accounts')))
        self.assertTrue(os.path.isdir(os.path.join(os.getcwd(), 'accounts', 'templates')))
        
    def test_generate_accounts_app_with_templates_with_dash_dasah_template(self):
        call_command('startaccountsapp', '--template')
        
        self.assertTrue(os.path.isdir(os.path.join(os.getcwd(), 'accounts')))
        self.assertTrue(os.path.isdir(os.path.join(os.getcwd(), 'accounts', 'templates')))
