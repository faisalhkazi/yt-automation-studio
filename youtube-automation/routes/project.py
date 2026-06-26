from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi import Request

from services.project_service import ProjectService

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/project/{project_id}")
async def project(request: Request, project_id: int):

    project = ProjectService.get(project_id)

    return templates.TemplateResponse(
            request=request,
            name="project.html",
            context={
                "project": project
                }
    )

