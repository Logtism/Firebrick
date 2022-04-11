from firebrick.api.endpoint import Endpoint
from firebrick.api.argparser import RequestParser


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