from sqlalchemy import Column, Integer, String

from service_database import Base


class DataBaseInfo(Base):
    __tablename__ = "database_info"

    id = Column(Integer, primary_key=True, index=True)
    db_type = Column(String)
    db_name = Column(String)
    host = Column(String)
    port = Column(Integer)

