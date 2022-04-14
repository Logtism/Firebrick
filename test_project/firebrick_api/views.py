from firebrick.api.endpoint import Endpoint
from firebrick.api.argparser import RequestParser
from firebrick.api.serializer import Serializer
from tests_test.models import Person


class test_endpoint(Endpoint):
    def POST(self, request):
        return {'success': True}


test_argparse_one_not_required_parser = RequestParser()
test_argparse_one_not_required_parser.add_argument('name', type=int)


    
class test_argparse_one_not_required(Endpoint):
    def POST(self, request):
        data = test_argparse_one_not_required_parser.parse(request)
        return {'success': True, 'name': data['name']}
    
    
test_argparse_one_required_parser = RequestParser()
test_argparse_one_required_parser.add_argument('name', type=int, required=True, help_msg='this is a test help msg')

    
class test_argparse_one_required(Endpoint):
    def POST(self, request):
        data = test_argparse_one_required_parser.parse(request)
        return {'success': True, 'name': data['name']}
   
   
test_argparse_two_required_parser = RequestParser()
test_argparse_two_required_parser.add_argument('name', type=int, required=True, help_msg='this is a test help msg')
test_argparse_two_required_parser.add_argument('name2', type=int, required=True, help_msg='this is a test help msg 2')
 
    
class test_argparse_two_required(Endpoint):
    def POST(self, request):
        data = test_argparse_one_required_parser.parse(request)
        return {'success': True, 'name': data['name'], 'name2': data['name2']}
    
    
class test_serializer_data(Serializer):
    class Meta:
        model = Person
        fields = ['id']
    

class test_serializer_data_view(Endpoint):
    def POST(self, request):
        person = Person.objects.create(name='helloworld')
        data = test_serializer_data.data(request)
        return {'success': True, 'id': data.id}
    

class test_serializer_parse(Serializer):
    class Meta:
        model = Person
        fields = ['id', 'name']
    

class test_serializer_parse_view(Endpoint):
    def POST(self, request):
        person = Person.objects.create(id=1, name='helloworld')
        data = test_serializer_parse.parse(person)
        return {'success': True, **data}