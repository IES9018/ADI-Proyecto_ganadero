from fastapi import FastAPI
from src.presentacion.api.routes import router

app = FastAPI(title="Ganadapp")

app.include_router(router)

@app.get("/")
def health():
    return {"status": "ok"}