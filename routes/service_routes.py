from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud
import schemas
from connections_to_databases import get_database, database
from models import databaseinfo
#from service_database import SessionLocal
from service_database import services_database

router = APIRouter()


# Создание служебной сессии для работы с нашей БД
#def service_db():
#    db = SessionLocal()
#    try:
#        yield db
#    finally:
#        db.close()


# Создание рабочей сессии для работы с БД аналитики
#def work_db():
#    db = get_database()
#    try:
#        yield db
#    finally:
#        db.close()


@router.get("/connect_info/", response_model=List[schemas.DateBaseInfo], tags=["CRUD for Service DB"])
async def get_connections():
    connections = databaseinfo.select()
    return await services_database.fetch_all(connections)


@router.post("/connect_info/", response_model=schemas.DateBaseInfo, tags=["CRUD for Service DB"])
async def create_db_connection(db_info: schemas.DateBaseCreate):
    return await crud.create_db_connect(db_info=db_info)


@router.get("/connect_info/{connect_id}", response_model=schemas.DateBaseInfo, tags=["CRUD for Service DB"])
async def get_connection(connect_id: int):
    return await crud.get_db_connect(connect_id=connect_id)


@router.patch("/connect_info/{connect_id}", response_model=schemas.DateBaseUpdate, tags=["CRUD for Service DB"])
async def update_db_connection(connect_id: int, db_info: schemas.DateBaseUpdate):
    update_info = db_info.dict(exclude_unset=True)
    return await crud.update_db_connect(connect_id=connect_id, db_info=update_info)


@router.delete("/connect_info/{connect_id}", tags=["CRUD for Service DB"])
async def delete_connection(connect_id: int):
    return await crud.delete_db_connect(connect_id=connect_id)

#
# @router.post("/create_connect/", tags=["Check connect to DB"])
# def create_connections(db_info: schemas.DateBaseCreate, db: Session = Depends(service_db)):
#     db_type = "postgresql"  # kwargs.get()
#     user = "kirill"
#     password = "kirill"  # kwargs.get()
#     server = "localhost"  # kwargs.get()
#     port = 5432  # kwargs.get()
#     db_name = "analitic"  # kwargs.get()
#     url = f"{db_type}://{user}:{password}@{server}:{port}/{db_name}"
#
#     database.create_connect(url)
#
#     return {'d': 3}
