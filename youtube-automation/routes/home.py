from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from services.project_service import ProjectService

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/")
async def home(request: Request):

    projects = ProjectService.list_projects()

    return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={
                "projects": projects
                }
            )



