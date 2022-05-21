import sqlalchemy

from service_database import engine

metadata = sqlalchemy.MetaData()


databaseinfo = sqlalchemy.Table(
    "database_info",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("db_type", sqlalchemy.String),
    sqlalchemy.Column("db_name", sqlalchemy.String),
    sqlalchemy.Column("host", sqlalchemy.String),
    sqlalchemy.Column("port", sqlalchemy.Integer),
)

metadata.create_all(engine)