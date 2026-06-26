from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from services.prompt_service import PromptService

router = APIRouter()


@router.get("/project/{project_id}/generate-prompts")
async def generate_prompts(project_id: int):

    PromptService.generate(project_id)

    return RedirectResponse(
        url=f"/project/{project_id}",
        status_code=303
    )
