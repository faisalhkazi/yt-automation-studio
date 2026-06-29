from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from services.video_service import VideoService

router = APIRouter()


@router.get("/project/{project_id}/generate-video")
async def generate_video(project_id: int):

    VideoService.generate(project_id)

    return RedirectResponse(
        url=f"/project/{project_id}",
        status_code=303
    )
