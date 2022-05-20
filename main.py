from typing import List

import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
# from connections_to_databases import
from connections_to_databases import get_database, db as db1
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()



if __name__ == "__main__":
    uvicorn.run(
        "main:app"
    )


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Dependency
def get_db_temp():
    db = get_database()
    try:
        yield db
    finally:
        db.close()


# @app.on_event("startup")
# async def startup():
#     await database.connect()
#     print("Подключение к базе")
#
#
# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()


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


@app.post("/test/")#response_model=schemas.DateBaseInfo)
def get_connections(db_info: schemas.DateBaseCreate, db: Session = Depends(get_db)):
    db_type = "postgresql+psycopg2" #kwargs.get()
    user = "portfolio"
    password = "portfolio"#kwargs.get()
    server = "localhost"#kwargs.get()
    port = 54321 #kwargs.get()
    db_name = "test_db"#kwargs.get()
    url = f"{db_type}://{user}:{password}@{server}:{port}/{db_name}"

    db1.create_connect(url)

    return {'d':3}

