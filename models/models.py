from datetime import datetime, timedelta
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

tags = Table()


class Log(Base):

    __tablename__ = 'logs'

    id          =   Column(Integer, primary_key=True)
    session_id  =   Column(String(36), nullable=False)
    date_time   = Column(DateTime, default=datetime.utcnow)


def init():
    # Create an engine that stores data in the local directory's
    # sqlalchemy_example.db file.
    engine = create_engine('sqlite:///sqlalchemy_example.db')

    # Create all tables in the engine. This is equivalent to "Create Table"
    # statements in raw SQL.
    Base.metadata.create_all(engine)

    return engine
