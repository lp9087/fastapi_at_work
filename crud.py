from fastapi import HTTPException
from sqlalchemy.orm import Session
import models, schemas
from service_database import services_database
from models import databaseinfo
from sqlalchemy import update


async def create_db_connect(db_info: schemas.DateBaseCreate):
    db_connect_create = databaseinfo.insert().values(id=db_info.id,
                                            db_type=db_info.db_type,
                                            db_name=db_info.db_name,
                                            host=db_info.host,
                                            port=db_info.port)
    db_connect_write = await services_database.execute(db_connect_create)
    return {**db_info.dict(), "id": db_connect_write}


async def get_db_connect(connect_id: int):
    query = databaseinfo.select().where(connect_id == databaseinfo.c.id)
    db_connect = await services_database.fetch_one(query=query)
    if db_connect is None:
        raise HTTPException(status_code=404, detail="Connection not found")
    return db_connect


async def update_db_connect(connect_id: int, db_info: schemas.DateBaseUpdate):
    query = databaseinfo.update().where(databaseinfo.c.id == connect_id).values(db_info)
    db_connect = await services_database.execute(query=query)
    if not db_connect:
        raise HTTPException(status_code=404, detail="Connection not found")
    res_query = databaseinfo.select().where(connect_id == databaseinfo.c.id)
    result = await services_database.fetch_one(query=res_query)
    return result


async def delete_db_connect(connect_id: int):
    query = databaseinfo.delete().where(connect_id == databaseinfo.c.id)
    db_connect = await services_database.execute(query=query)
    if not db_connect:
        raise HTTPException(status_code=404, detail="Connection not found")
    return {f"Delete id {connect_id}": "Complete"}



async def test(db: Session, skip: int = 0, limit: int = 100):
    pass
