from django.test import TestCase, Client
from django.urls import reverse, resolve
from firebrick.tests import ResolveUrlTest
from . import views
import json


class TestTestEndpoint(TestCase, ResolveUrlTest):
    name = 'api-test-endpoint'
    view = views.test_endpoint.handler

    def test_invalid_method_GET(self):
        client = Client()

        url = reverse(self.name)

        response = client.get(url)

        self.assertEquals(response.status_code, 405)
        self.assertEquals(response.content, b'{"success": false, "error_message": "Method is not allowed."}')

    def test_invalid_method_PUT(self):
        client = Client()

        url = reverse(self.name)

        response = client.put(url)

        self.assertEquals(response.status_code, 405)
        self.assertEquals(response.content, b'{"success": false, "error_message": "Method is not allowed."}')

    def test_invalid_method_PATCH(self):
        client = Client()

        url = reverse(self.name)

        response = client.patch(url)

        self.assertEquals(response.status_code, 405)
        self.assertEquals(response.content, b'{"success": false, "error_message": "Method is not allowed."}')

    def test_invalid_method_DELETE(self):
        client = Client()

        url = reverse(self.name)

        response = client.delete(url)

        self.assertEquals(response.status_code, 405)
        self.assertEquals(response.content, b'{"success": false, "error_message": "Method is not allowed."}')

    def test_valid_method_POST(self):
        client = Client()

        url = reverse(self.name)

        response = client.post(url)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, b'{"success": true}')
        
        
class TestArgParserOneNotRequired(TestCase, ResolveUrlTest):
    name = 'api-argparser-one-not-required'
    view = views.test_argparse_one_not_required.handler
    
    def test_not_sending_json_body(self):
        client = Client()
        
        url = reverse(self.name)
        
        response = client.post(url)
        
        self.assertEquals(response.content, b'{"success": false, "error_message": "Body is not valid json."}')
        self.assertEquals(response.status_code, 400)
        
    def test_sending_valid_json_without_name_field(self):
        client = Client()
        
        url = reverse(self.name)
        
        response = client.post(url, {}, content_type="application/json")
        
        self.assertEquals(response.content, b'{"success": true, "name": null}')
        self.assertEquals(response.status_code, 200)
        
    def test_sending_valid_json_with_name_field_incorrect_type(self):
        client = Client()
        
        url = reverse(self.name)
        
        response = client.post(url, {'name': 'testing123'}, content_type="application/json")
        
        self.assertEquals(response.content, b'{"success": false, "error_message": "name is not type int"}')
        self.assertEquals(response.status_code, 400)
        
    def test_sending_valid_json_with_name_field_correct_type(self):
        client = Client()
        
        url = reverse(self.name)
        
        response = client.post(url, {'name': 22}, content_type="application/json")
        
        self.assertEquals(response.status_code, 200)
        self.assertIn('name', json.loads(response.content))
        self.assertEquals(json.loads(response.content)['name'], 22)