from fastapi import APIRouter, UploadFile, File, HTTPException, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from services.image_upload_service import ImageUploadService
from services.scene_service import SceneService
from services.project_service import ProjectService
from services.workflow_service import WorkflowService

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/project/{project_id}/upload-images")
async def upload_images_page(
    request: Request,
    project_id: int
):

    project = ProjectService.get(project_id)

    workflow = WorkflowService.status(project_id)

    return templates.TemplateResponse(
            request=request,
            name="project/upload_images.html",
            context={
                "project": project,
                "workflow": workflow
                }
            )



@router.get("/project/{project_id}/replace-image/{scene}")
async def replace_image_page(
    request: Request,
    project_id: int,
    scene: int
):

    project = ProjectService.get(project_id)

    return templates.TemplateResponse(
        request=request,
        name="project/replace_image.html",
        context={
            "project": project,
            "scene": scene
        }
    )

@router.post("/project/{project_id}/replace-image/{scene}")
async def replace_image(
    project_id: int,
    scene: int,
    image: UploadFile = File(...)
):

    ImageUploadService.replace(
        project_id,
        scene,
        image
    )

    return RedirectResponse(
        url=f"/project/{project_id}/timeline",
        status_code=303
    )


@router.post("/project/{project_id}/upload-images")
async def upload_images(
    project_id: int,
    files: list[UploadFile] = File(...)
):

    required = SceneService.count(project_id)

    if len(files) != required:
        raise HTTPException(
            status_code=400,
            detail=f"Please upload exactly {required} images."
        )

    ImageUploadService.upload(
        project_id,
        files
    )

    return RedirectResponse(
            url=f"/project/{project_id}?success=images_uploaded",
            status_code=303
            )

