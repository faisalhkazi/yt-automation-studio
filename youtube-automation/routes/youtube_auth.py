from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from providers.youtube.oauth_service import OAuthService

router = APIRouter()


@router.get("/youtube/connect")
async def youtube_connect():

    url = OAuthService.get_authorization_url()

    return RedirectResponse(url)
