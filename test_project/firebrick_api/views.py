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