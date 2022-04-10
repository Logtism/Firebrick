from django.test import TestCase, Client
from django.urls import reverse, resolve
from firebrick.tests import ResolveUrlTest
from . import views


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