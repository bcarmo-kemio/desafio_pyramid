from wsgiref.simple_server import make_server
from pyramid.session import SignedCookieSessionFactory
from static import COOKIE_KEY
import routes


if __name__ == '__main__':
    sessions = SignedCookieSessionFactory(COOKIE_KEY)  # Creating a session factory
    config = routes.init()
    config.set_session_factory(sessions)
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
