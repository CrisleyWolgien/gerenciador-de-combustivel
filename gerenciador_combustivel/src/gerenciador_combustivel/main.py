from dotenv import load_dotenv
from fastapi import FastAPI

from src.gerenciador_combustivel.core.db import init_db

load_dotenv()

app = FastAPI()


@app.get("/ping")
def ping():
    return {"status": "ok"}
