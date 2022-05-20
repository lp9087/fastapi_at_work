from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import databases


#def change_engine(db, db_info):
#    db_type = db_info.db_type               #"postgresql+psycopg2" #kwargs.get()
#    user = db_info.user                     #"postgres"
#    password = db_info.password                #"postgres"#kwargs.get()
#    server = db_info.server                   #"localhost"#kwargs.get()
#    port = db_info.port                      #5432 #kwargs.get()
#    db_name = db_info.db_name                    #"test_db"#kwargs.get()
#    return db_type, user, password, server, port, db_name

db_type = "postgresql+psycopg2" #kwargs.get()
user = "postgres"
password = "postgres"#kwargs.get()
server = "localhost"#kwargs.get()
port = 5432 #kwargs.get()
db_name = "test_db"#kwargs.get()


DATABASE_URL = f"{db_type}://{user}:{password}@{server}:{port}/{db_name}"

database = databases.Database(DATABASE_URL)

engine = create_engine(DATABASE_URL, echo=True)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    connection = engine.connect()
    transaction = connection.begin()
    db = TestingSessionLocal(bind=connection)
    yield db
    db.rollback()
    connection.close()




