from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

# Создание сессии для работы с БД аналитики


class DataBaseCreate:
    session = None

    @classmethod
    def create_connect(cls, url):
        engine = create_async_engine(url, echo=True)
        cls.session = sessionmaker(bind=engine, class_=AsyncSession, autocommit=False, autoflush=False)


database_con = DataBaseCreate()


def get_database_con():
    return database_con.session()




