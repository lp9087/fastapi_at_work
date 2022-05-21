from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
import crud
import models
import schemas
from connections_to_databases import get_database_con, database_con
from service_database import SessionLocal, engine


router = APIRouter()


# Создание служебной сессии для работы с нашей БД
async def service_db() -> AsyncSession:
    async with SessionLocal() as session:
        try:
            yield session
        finally:
            session.close()


# Создание рабочей сессии для работы с БД аналитики
async def work_db() -> AsyncSession:
    async with get_database_con() as session_work:
        try:
            yield session_work
        finally:
            session_work.close()


@router.get("/connect_info/", response_model=List[schemas.DateBaseInfo], tags=["CRUD for Service DB"])
async def get_connections(db: AsyncSession = Depends(service_db)):
    return await crud.get_db_connects(db=db)


@router.post("/connect_info/", response_model=schemas.DateBaseInfo, tags=["CRUD for Service DB"])
async def create_db_connection(db_info: schemas.DateBaseCreate, db: AsyncSession = Depends(work_db)):
    return await crud.create_db_connect(db_info=db_info, db=db)


@router.get("/connect_info/{connect_id}", response_model=schemas.DateBaseInfo, tags=["CRUD for Service DB"])
async def get_connection(connect_id: int, db: AsyncSession = Depends(service_db)):
    return await crud.get_db_connect(connect_id=connect_id, db=db)


@router.patch("/connect_info/{connect_id}", response_model=schemas.DateBaseUpdate, tags=["CRUD for Service DB"])
async def update_db_connection(connect_id: int, db_info: schemas.DateBaseUpdate, db: AsyncSession = Depends(service_db)):
    update_info = db_info.dict(exclude_unset=True)
    return await crud.update_db_connect(connect_id=connect_id, db_info=update_info, db=db)


@router.delete("/connect_info/{connect_id}", tags=["CRUD for Service DB"])
async def delete_connection(connect_id: int, db: AsyncSession = Depends(service_db)):
    return await crud.delete_db_connect(connect_id=connect_id, db=db)


@router.post("/create_connect/", tags=["Check connect to DB"])
async def create_connections(db_info: schemas.DateBaseCreate, db: AsyncSession = Depends(service_db)):
    db_type = "postgresql+asyncpg"  # kwargs.get()
    user = "kirill"
    password = "kirill"  # kwargs.get()
    server = "localhost"  # kwargs.get()
    port = 5432  # kwargs.get()
    db_name = "analitic"  # kwargs.get()
    url = f"{db_type}://{user}:{password}@{server}:{port}/{db_name}"

    database_con.create_connect(url)

    return {'d': 3}
