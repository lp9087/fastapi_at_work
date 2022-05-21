import databases
import sqlalchemy

# Создание сессии для работы со служебной БД

DATABASE_URL = "sqlite:///./sql_app_async.db"

services_database = databases.Database(DATABASE_URL)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)


#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base = declarative_base()
