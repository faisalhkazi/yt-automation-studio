from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from services.project_service import ProjectService
from services.script_service import ScriptService
from providers.tts.piper_provider import PiperService


router = APIRouter()


@router.post("/generate")
async def generate(
    title: str = Form(...),
    category: str = Form(...),
    script: str = Form(...)
):

    # Create project in database
    project_id = ProjectService.create(
        title,
        category,
        script
    )

    # Save script to file
    script_path = ScriptService.save(
    project_id,
    script
    )

    # Update database with script path
    ProjectService.update_script(
        project_id,
        script_path.relative_to(script_path.parents[2]).as_posix()
    )

    # Generate audio
    audio_path = PiperService.generate(
    project_id,
    script_path
    )

    # Update database with audio path
    ProjectService.update_audio(
        project_id,
        audio_path.relative_to(audio_path.parents[2]).as_posix()
    )
    

    return RedirectResponse(
    url=f"/project/{project_id}",
    status_code=303
    )


