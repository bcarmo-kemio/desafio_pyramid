from pyramid.config import Configurator


def init():
    with Configurator() as config:
        config.add_route('hello',         '/')
        config.add_route('quotes',        '/quotes')
        config.add_route('random_quotes', '/quotes/random')
        config.add_route('quotes:id',     '/quotes/{id}')
        config.scan('views')
    return config
