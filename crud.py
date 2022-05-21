from fastapi import HTTPException
from sqlalchemy.orm import Session

import models, schemas


def create_db_connect(db: Session, db_info: schemas.DateBaseCreate):
    db_connect_create = models.DataBaseInfo(id=db_info.id,
                                            db_type=db_info.db_type,
                                            db_name=db_info.db_name,
                                            host=db_info.host,
                                            port=db_info.port)
    db.add(db_connect_create)
    db.commit()
    db.refresh(db_connect_create)
    return db_connect_create


def get_db_connections(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.DataBaseInfo).offset(skip).limit(limit).all()


def get_db_connect(db: Session, connect_id: int):
    db_connect = db.query(models.DataBaseInfo).filter(models.DataBaseInfo.id == connect_id).first()
    if db_connect is None:
        raise HTTPException(status_code=404, detail="Connection not found")
    return db_connect


def update_db_connect(db: Session, connect_id: int, db_info: schemas.DateBaseUpdate):
    db_connect = db.query(models.DataBaseInfo).filter(models.DataBaseInfo.id == connect_id).one_or_none()
    if db_connect is None:
        raise HTTPException(status_code=404, detail="Connect not found")
    for key, value in db_info.items():
        setattr(db_connect, key, value)
    db.add(db_connect)
    db.commit()
    db.refresh(db_connect)
    return db_connect


def delete_db_connect(db: Session, connect_id: int):
    db_connect = db.query(models.DataBaseInfo).filter(models.DataBaseInfo.id == connect_id).one_or_none()
    if db_connect is None:
        raise HTTPException(status_code=404, detail="Connect not found")
    db.delete(db_connect)
    db.commit()
    return {"Delete": "Complete"}


async def test(db: Session, skip: int = 0, limit: int = 100):
    pass
