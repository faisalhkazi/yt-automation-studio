from fastapi import FastAPI
from routes.project import router as project_router
from routes.home import router as home_router
from routes.generate import router as generate_router

from services.project_service import ProjectService

app = FastAPI(title="YT Automation")

ProjectService.initialize()

app.include_router(home_router)
app.include_router(generate_router)
app.include_router(project_router)
