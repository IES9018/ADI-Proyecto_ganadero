from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from src.routes.animal_routes import router as animal_router
from src.routes.sanidad_routes import router as sanidad_router

app = FastAPI()

app.include_router(animal_router)
app.include_router(sanidad_router)

app.mount("/static", StaticFiles(directory="src/static"), name="static")


# única página del sistema
@app.get("/")
def home():
    return FileResponse("src/templates/index.html")