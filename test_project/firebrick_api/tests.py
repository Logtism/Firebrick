from django.test import TestCase, Client
from django.urls import reverse, resolve
from firebrick.tests import ResolveUrlTest
from tests_test.models import Person
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
        
        
class TestArgParserOneRequired(TestCase, ResolveUrlTest):
    name = 'api-argparser-one-required'
    view = views.test_argparse_one_required.handler
    
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
        
        self.assertEquals(response.content, b'{"success": false, "error_message": "this is a test help msg"}')
        self.assertEquals(response.status_code, 400)
        
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
        
        
class TestSerializerData(TestCase, ResolveUrlTest):
    name = 'api-test-serializer-data'
    view = views.test_serializer_data_view.handler
    
    def test_not_sending_json_body(self):
        client = Client()
        
        url = reverse(self.name)
        
        response = client.post(url)
        
        self.assertEquals(response.content, b'{"success": false, "error_message": "Body is not valid json."}')
        self.assertEquals(response.status_code, 400)
        
    def test_sending_valid_json_without_id_field(self):
        client = Client()
        
        url = reverse(self.name)
        
        response = client.post(url, {}, content_type="application/json")
        
        self.assertEquals(response.content, b'{"success": false, "error_message": "id is required."}')
        self.assertEquals(response.status_code, 400)
        
    def test_sending_valid_json_with_incorrect_id_type(self):
        client = Client()
        
        url = reverse(self.name)
        
        response = client.post(url, {'id': 'nonono'}, content_type="application/json")

        self.assertEquals(response.content, b'{"success": false, "error_message": "Not all arguments were the correct type."}')
        self.assertEquals(response.status_code, 400)
        
    def test_sending_valiid_json_with_id_that_does_not_exist(self):
        client = Client()
        
        url = reverse(self.name)
        
        response = client.post(url, {'id': 10}, content_type="application/json")
        
        self.assertEquals(response.status_code, 404)
        
    def test_sending_valiid_json_with_id_that_does_exist(self):
        person = Person.objects.create(id=1, name='test')
        
        client = Client()
        
        url = reverse(self.name)
        
        response = client.post(url, {'id': person.id}, content_type="application/json")
        
        self.assertEquals(response.status_code, 200)
        self.assertIn('id', json.loads(response.content))
        self.assertEquals(person.id, json.loads(response.content)['id'])
        

class TestSerializerParse(TestCase, ResolveUrlTest):
    name = 'api-test-serializer-parse'
    view = views.test_serializer_parse_view.handler
    
    def test_correct_data(self):
        client = Client()
        
        url = reverse(self.name)
        
        response = client.post(url)
        
        self.assertEquals(response.status_code, 200)
        
        self.assertIn('id', json.loads(response.content))
        self.assertEquals(1, json.loads(response.content)['id'])
        
        self.assertIn('name', json.loads(response.content))
        self.assertEquals('helloworld', json.loads(response.content)['name'])