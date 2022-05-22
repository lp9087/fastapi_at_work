from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
import models, schemas
from sqlalchemy import select


async def get_db_connect(connect_id: int, db: AsyncSession):
    cursor = await db.execute(select(models.DataBaseInfo).where(models.DataBaseInfo.id == connect_id))
    data = cursor.scalars().first()
    if not data:
        raise HTTPException(status_code=404, detail="Connection not found")
    return data


async def create_db_connect(db_info: schemas.DateBaseCreate, db: AsyncSession):
    db_connect_create = models.DataBaseInfo(id=db_info.id,
                                            db_type=db_info.db_type,
                                            db_name=db_info.db_name,
                                            host=db_info.host,
                                            port=db_info.port)
    db.add(db_connect_create)
    await db.commit()
    await db.refresh(db_connect_create)
    return db_connect_create


async def get_db_connects(db: AsyncSession):
    cursor = await db.execute(select(models.DataBaseInfo))
    data = cursor.scalars().all()
    return data


async def update_db_connect(connect_id: int, db_info: schemas.DateBaseUpdate, db: AsyncSession):
    data = await get_db_connect(connect_id=connect_id, db=db)
    for key, value in db_info.items():
        setattr(data, key, value)
    db.add(data)
    await db.commit()
    return db_info


async def delete_db_connect(connect_id: int, db: AsyncSession):
    data = await get_db_connect(connect_id=connect_id, db=db)
    await db.delete(data)
    await db.commit()
    return {f"{connect_id}": "Delete"}


async def test(db: Session, skip: int = 0, limit: int = 100):
    pass
