class P3PCPMiddleware(object):
    def process_response(self, request, response):
        response['P3P'] = 'CP="foobar"'
        return response
