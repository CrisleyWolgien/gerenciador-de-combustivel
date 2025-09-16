from dotenv import load_dotenv
from fastapi import FastAPI
from .routers import (user_route,SupplyRouter,vehicleRouter)

load_dotenv()

app = FastAPI()


@app.get("/ping")
def ping():
    return {"status": "ok"}


app.include_router(SupplyRouter.router)
app.include_router(user_route.router)
app.include_router(vehicleRouter.router)