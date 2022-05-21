from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Создание сессии для работы с БД аналитики


class DataBase:
    session = None

    @classmethod
    def create_connect(cls, url):
        engine = create_engine(url, echo=True)
        cls.session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


database = DataBase()


def get_database():
    return database.session()




