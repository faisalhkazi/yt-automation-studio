from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from services.timeline_service import TimelineService
from services.timeline_preview_service import TimelinePreviewService
from services.project_service import ProjectService

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/project/{project_id}/generate-timeline")
async def generate_timeline(project_id: int):

    TimelineService.generate(project_id)

    return RedirectResponse(
        url=f"/project/{project_id}/timeline",
        status_code=303
    )


@router.get("/project/{project_id}/timeline")
async def timeline_preview(
    request: Request,
    project_id: int
):

    project = ProjectService.get(project_id)

    timeline = TimelinePreviewService.load(project_id)

    
    return templates.TemplateResponse(
            request=request,
            name="project/timeline.html",
            context={
                "project": project,
                "timeline": timeline
                }
            )

