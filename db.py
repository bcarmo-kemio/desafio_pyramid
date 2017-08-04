# Initializing DB
from sqlalchemy.orm import sessionmaker

from models import models


class DbManager:
    __instance = None

    def __new__(cls):
        if DbManager.__instance is None:
            DbManager.__instance = sessionmaker(bind=models.init())()

        return DbManager.__instance