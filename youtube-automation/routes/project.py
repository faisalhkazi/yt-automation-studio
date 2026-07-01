from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from services.scene_preview_service import ScenePreviewService
from services.project_service import ProjectService
from services.workflow_service import WorkflowService



router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/project/{project_id}")
async def project(
    request: Request,
    project_id: int,
    success: str | None = None
):

    project = ProjectService.get(project_id)

    workflow = WorkflowService.status(project_id)

    scenes = ScenePreviewService.load(project_id)



    return templates.TemplateResponse(
            request=request,
            name="project/overview.html",
            context={
                "project": project,
                "workflow": workflow,
                "scenes": scenes,
                "success": success
                }
            )



