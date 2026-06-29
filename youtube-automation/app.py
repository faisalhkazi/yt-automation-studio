from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.project import router as project_router
from routes.home import router as home_router
from routes.generate import router as generate_router
from routes.script import router as script_router
from services.project_service import ProjectService
from routes.scenes import router as scenes_router
from routes.prompts import router as prompts_router
from routes.images import router as images_router
from routes.video import router as video_router
from routes.timeline import router as timeline_router
from routes.images import router as images_router
from routes.wizard import router as wizard_router



app = FastAPI(title="YT Automation")

ProjectService.initialize()

app.mount(
    "/storage",
    StaticFiles(directory="storage"),
    name="storage"
)

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

app.include_router(home_router)
app.include_router(generate_router)
app.include_router(project_router)
app.include_router(script_router)
app.include_router(scenes_router)
app.include_router(prompts_router)
app.include_router(images_router)
app.include_router(timeline_router)
app.include_router(video_router)
app.include_router(wizard_router)


