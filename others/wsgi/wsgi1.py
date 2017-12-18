from wsgiref.simple_server import make_server

def application(environ, start_response):
    response_body = [
        '%s: %s' %(key, value) for key, value in sorted(environ.items())
    ]

    response_body = '\n'.join(response_body)

    response_body = [
        'The Beggining\n',
        '*' * 30 + '\n',
        response_body,
        '\n' + '*' * 30 ,
        '\nThe End'
    ]

    content_length = sum([len(s) for s in response_body])


    status = '200 OK'

    response_header = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_header)

    return response_body

httpd = make_server(
    'localhost',
    8051,
    application
)

print "Server Running on Port:8051"
httpd.handle_request()
