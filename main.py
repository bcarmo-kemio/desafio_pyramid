from wsgiref.simple_server import make_server
import routes


# code to run if called on terminal
if __name__ == '__main__':
    config = routes.init()
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
