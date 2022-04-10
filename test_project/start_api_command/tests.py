from django.test import TestCase
from django.core.management.base import CommandError
from django.core.management import call_command
import firebrick
import shutil
import os


class TestStartApiCommand(TestCase):
    def tearDown(self):
        if os.path.isdir(os.path.join(os.getcwd(), 'api')):
            shutil.rmtree(os.path.join(os.getcwd(), 'api'))

    def test_generate_api_invalid_name(self):
        with self.assertRaises(CommandError) as context:
            call_command('startapi', 'django')

        self.assertFalse(os.path.isdir(os.path.join(os.getcwd(), 'api')))

    def test_generate_api_valid_name(self):
        call_command('startapi', 'testing')

        api_name = 'testing'

        self.assertTrue(os.path.isdir(os.path.join(os.getcwd(), 'api')))
        self.assertTrue(os.path.isdir(os.path.join(os.getcwd(), 'api', api_name)))

        api_template_path = os.path.join(firebrick.__path__[0], 'templates', 'api')

        for file in [f for f in os.listdir(os.path.join(api_template_path)) if os.path.isfile(os.path.join(api_template_path, f))]:
            self.assertTrue(os.path.isfile(os.path.join(api_template_path, file)))