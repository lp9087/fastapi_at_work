from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from connections_to_databases import override_get_db, database
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
async def startup():
    await database.connect()
    print("Подключение к базе")


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/db_connect/", response_model=List[schemas.DateBaseInfo])
def get_connections(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_db_connections(db, skip=skip, limit=limit)


@app.post("/db_connect/", response_model=schemas.DateBaseInfo)
def create_db_connection(db_info: schemas.DateBaseCreate, db: Session = Depends(get_db)):
    return crud.create_db_connect(db=db, db_info=db_info)


@app.get("/db_connect/{connect_id}", response_model=schemas.DateBaseInfo)
def get_connection(connect_id: int, db: Session = Depends(get_db)):
    return crud.get_db_connect(db, connect_id=connect_id)


@app.patch("/db_connect/{connect_id}", response_model=schemas.DateBaseInfo)
def update_db_connection(connect_id: int, db_info: schemas.DateBaseUpdate, db: Session = Depends(get_db)):
    update_info = db_info.dict(exclude_unset=True)
    return crud.update_db_connect(db=db, connect_id=connect_id, db_info=update_info)


@app.delete("/db_connect/{connect_id}")
def delete_connection(connect_id: int, db: Session = Depends(get_db)):
    return crud.delete_db_connect(db=db, connect_id=connect_id)


#@app.post("/test/", response_model=schemas.DateBaseInfo)
#async def get_connections(db_info: schemas.DateBaseCreate, db: Session = Depends(override_get_db)):
#    await change_engine(db, db_info=db_info)
