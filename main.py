import uvicorn
from fastapi import FastAPI
from routes import service_routes

app = FastAPI()

app.include_router(service_routes.router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app", reload=True
    )
