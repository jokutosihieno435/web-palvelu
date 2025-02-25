
def app(environ, respond):
    respond('200 OK', [('Content-type', 'text/html; charset=utf-8')])
    nimi = environ['PATH_INFO'].strip('/')
    yield "<h1>huomio!</h1>".encode('utf-8')
    yield ("<p><em>nimesi</em> on: %s</p>" % nimi).encode('utf-8')

