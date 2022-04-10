from firebrick.api.endpoint import Endpoint


class test_endpoint(Endpoint):
    def POST(self):
        return {'success': True}