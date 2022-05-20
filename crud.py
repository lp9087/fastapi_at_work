from fastapi import HTTPException
from sqlalchemy.orm import Session

import models, schemas


# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()
#
#
# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()
#
#
# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()
#
#
# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user
#
#
# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()
#
#
# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item


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
