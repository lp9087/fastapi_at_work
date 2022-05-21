import uvicorn
from fastapi import FastAPI
from routes import service_routes
from service_database import init_db

app = FastAPI()

app.include_router(service_routes.router)


@app.on_event("startup")
async def on_startup():
    await init_db()


if __name__ == "__main__":
    uvicorn.run(
        "main:app", reload=True
    )
