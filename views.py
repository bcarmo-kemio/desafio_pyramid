from pyramid.response import Response
from pyramid.view import view_config
from requests import HTTPError

from db import DbManager
from desafioapi import DesafioAPI
from uuid import uuid4
from models.models import Log
import random


class MyViews:
    def __init__(self, request):
        self.request = request
        self.session = request.session

        self.db = DbManager()

        if not self.session:
            self.session['user'] = uuid4()

        if "logs" not in self.request.path:
            # Creating model and inserting it on the db
            log_entry = Log(session_id=str(self.session['user']), date_time=None, page=self.request.path)

            self.db.add(log_entry)
            self.db.commit()

    @view_config(route_name='quotes:id', renderer='json')
    def get_quotes(self):
        quote_id = self.request.matchdict.get('id', '')
        try:
            html = "<li>{0}</li>".format(DesafioAPI.do_request(quote_id)['quote'])
        except HTTPError:
            html = "<p>Nenhuma quote foi encontrada com esse id</p>"

        return Response(html)

    @view_config(route_name='quotes')
    def get_quote(self):
        html = "<ul>"
        for q in DesafioAPI.do_request()['quotes']:
            html += "<li>{0}</li>".format(q)
        html += "</ul>"
        return Response(html)

    @view_config(route_name='random_quotes', renderer='json')
    def get_random_quote(self):
        all_quotes = DesafioAPI.do_request()['quotes']
        return all_quotes[random.randint(0, len(all_quotes) - 1)]

    @view_config(route_name='hello')
    def hello(self):
        return Response("<h1>Desafio Web 1.0</h1>")

    @view_config(route_name='session-log:id')
    def session_log(self):
        log_id = self.request.matchdict.get('id', False)
        operation = self.request.matchdict.get('operation')

        log_element = Log()

        if log_id:
            log_element.id = log_id

        # TODO: Come up with a better way to do this:
        if operation == 'list':
            resp = DbManager().query(Log).get(log_id)
            if resp is None:
                resp = 'Nenhum log foi encontrado com esse id'

            html = '<li>{0}</li>'.format(str(resp))
            return Response(html)

        elif operation == 'delete':
            c = 3

    @view_config(route_name='sessions-logs')
    def sessions_logs(self):
        operation = self.request.matchdict.get('operation')

        if operation == 'list':
            resp = DbManager().query(Log).all()
            if resp is None:
                resp = 'Nenhum log foi encontrado'

            html = '<ul>'
            for log in resp:
                html += '<li>{0}</li>'.format(str(log))
            html += '</ul>'

            return Response(html)

        elif operation == 'delete':
            c = 3

