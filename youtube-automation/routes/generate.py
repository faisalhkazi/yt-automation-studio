from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from services.project_service import ProjectService
from services.script_service import ScriptService
from services.piper_service import PiperService

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
    script_path = ScriptService.save(script)

    # Update database with script path
    ProjectService.update_script(
        project_id,
        str(script_path)
    )

    # Generate audio
    audio_path = PiperService.generate(script_path)

    # Update database with audio path
    ProjectService.update_audio(
        project_id,
        str(audio_path)
    )
    

    return RedirectResponse(
    url="/",
    status_code=303
    )


