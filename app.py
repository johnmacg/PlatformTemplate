# uwsgi requires the WSGI entry point to be named "application"
def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'Hello World and Welcome to Platform.sh!!']
