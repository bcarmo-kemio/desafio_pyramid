from datetime import datetime
from sqlalchemy import Table, Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
tags = Table()


class Log(Base):

    __tablename__ = 'logs'

    id          =   Column(Integer, primary_key=True)
    session_id  =   Column(String(36))
    date_time   =   Column(DateTime, default=datetime.utcnow)
    page        =   Column(String(50))

    def __str__(self):
        model = 'Sessão: {0},  Data: {1}, Consulta: {2}'
        formated_date = self.date_time.strftime('%m/%d/%Y - %Hh%M')
        return model.format(self.session_id, formated_date , self.page)


def init():
    # Create an engine that stores data in the local directory's
    # sqlalchemy_example.db file.
    engine = create_engine('sqlite:///sqlalchemy_example.db')

    Base.metadata.bind = engine

    # Create all tables in the engine. This is equivalent to "Create Table"
    # statements in raw SQL.
    Base.metadata.create_all(engine)

    return engine
