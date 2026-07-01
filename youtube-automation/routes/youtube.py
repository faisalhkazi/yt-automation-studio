from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from services.youtube_service import YouTubeService

router = APIRouter()


@router.get("/youtube/connect")
async def connect():

    url = YouTubeService.authorization_url()

    return RedirectResponse(url)
