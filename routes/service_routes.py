from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud
import schemas
from connections_to_databases import get_database, database
from service_database import SessionLocal

router = APIRouter()


# Создание служебной сессии для работы с нашей БД
def service_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Создание рабочей сессии для работы с БД аналитики
def work_db():
    db = get_database()
    try:
        yield db
    finally:
        db.close()


@router.get("/connect_info/", response_model=List[schemas.DateBaseInfo], tags=["CRUD for Service DB"])
def get_connections(skip: int = 0, limit: int = 100, db: Session = Depends(service_db)):
    return crud.get_db_connections(db, skip=skip, limit=limit)


@router.post("/connect_info/", response_model=schemas.DateBaseInfo, tags=["CRUD for Service DB"])
def create_db_connection(db_info: schemas.DateBaseCreate, db: Session = Depends(service_db)):
    f = 5
    return crud.create_db_connect(db=db, db_info=db_info)


@router.get("/connect_info/{connect_id}", response_model=schemas.DateBaseInfo, tags=["CRUD for Service DB"])
def get_connection(connect_id: int, db: Session = Depends(service_db)):
    return crud.get_db_connect(db, connect_id=connect_id)


@router.patch("/connect_info/{connect_id}", response_model=schemas.DateBaseInfo, tags=["CRUD for Service DB"])
def update_db_connection(connect_id: int, db_info: schemas.DateBaseUpdate, db: Session = Depends(service_db)):
    update_info = db_info.dict(exclude_unset=True)
    return crud.update_db_connect(db=db, connect_id=connect_id, db_info=update_info)


@router.delete("/connect_info/{connect_id}", tags=["CRUD for Service DB"])
def delete_connection(connect_id: int, db: Session = Depends(service_db)):
    return crud.delete_db_connect(db=db, connect_id=connect_id)


@router.post("/create_connect/", tags=["Check connect to DB"])
def create_connections(db_info: schemas.DateBaseCreate, db: Session = Depends(service_db)):
    db_type = "postgresql"  # kwargs.get()
    user = "kirill"
    password = "kirill"  # kwargs.get()
    server = "localhost"  # kwargs.get()
    port = 5432  # kwargs.get()
    db_name = "analitic"  # kwargs.get()
    url = f"{db_type}://{user}:{password}@{server}:{port}/{db_name}"

    database.create_connect(url)

    return {'d': 3}
