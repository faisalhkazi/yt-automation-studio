from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from services.youtube_settings_service import (
    YouTubeSettingsService
)

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/settings/youtube")
async def youtube_settings(request: Request):

    settings = YouTubeSettingsService.get()

    return templates.TemplateResponse(
        request=request,
        name="settings/youtube.html",
        context={
            "request": request,
            "settings": settings
        }
    )
