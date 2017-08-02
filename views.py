from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy.orm import sessionmaker

from prova import Prova
from uuid import uuid4
from models import models
import random


class MyViews:
    def __init__(self, request):
        self.request = request
        self.session = request.session

        # Initializing DB
        DBSession = sessionmaker(bind=models.init())  # TODO: arrumar init para ser singleton
        session = DBSession()

        if not self.session:
            self.session['user'] = uuid4()

        # Creating model and inserting it on the db
        log_entry = models.Log(session_id=str(self.session['user']), date_time=None)
        session.add(log_entry)
        session.commit()

    @view_config(route_name='quotes:id', renderer='json')
    def get_quotes(self):
        quote_id = self.request.matchdict.get('id', '')
        html = "<li>%s</li>" % Prova.do_request(quote_id)['quote']
        return Response(html)

    @view_config(route_name='quotes')
    def get_quote(self):
        html = "<ul>"
        for q in Prova.do_request()['quotes']:
            html += "<li>%s</li>" % q
        html += "</ul>"
        return Response(html)

    @view_config(route_name='random_quotes', renderer='json')
    def get_random_quote(self):
        all_quotes = Prova.do_request()['quotes']
        return all_quotes[random.randint(0, len(all_quotes) - 1)]

    @view_config(route_name='hello')
    def hello(self):
        return Response("<h1>Desafio Web 1.0</h1>")
