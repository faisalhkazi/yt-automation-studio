from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from services.project_service import ProjectService
from services.script_service import ScriptService
from providers.tts.piper_provider import PiperService

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/wizard")
async def wizard(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="wizard/step1.html",
        context={}
    )


@router.post("/wizard/create")
async def create_project(

    title: str = Form(...),
    category: str = Form(...),
    script: str = Form(...)

):

    project_id = ProjectService.create(
        title,
        category,
        script
    )

    script_path = ScriptService.save(
        project_id,
        script
    )

    ProjectService.update_script(
        project_id,
        script_path.relative_to(script_path.parents[2]).as_posix()
    )

    audio_path = PiperService.generate(
        project_id,
        script_path
    )

    ProjectService.update_audio(
        project_id,
        audio_path.relative_to(audio_path.parents[2]).as_posix()
    )

    return RedirectResponse(
        url=f"/project/{project_id}",
        status_code=303
    )
