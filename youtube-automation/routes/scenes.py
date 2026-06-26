from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from services.scene_service import SceneService

router = APIRouter()


@router.get("/project/{project_id}/generate-scenes")
async def generate_scenes(project_id: int):

    SceneService.generate(project_id)

    return RedirectResponse(
        url=f"/project/{project_id}",
        status_code=303
    )
