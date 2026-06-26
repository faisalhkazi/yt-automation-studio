from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/script/{project_id}")
def view_script(project_id: int):

    from services.project_service import ProjectService

    project = ProjectService.get(project_id)

    if not project:
        raise HTTPException(status_code=404)

    script_file = Path(project["script_file"])

    if not script_file.exists():
        raise HTTPException(status_code=404)

    script = script_file.read_text(encoding="utf-8")

    return HTMLResponse(f"""
    <html>

    <head>

    <title>Script</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

    </head>

    <body class="bg-light">

    <div class="container mt-5">

        <div class="card shadow">

            <div class="card-header">

                <h2>{project["title"]}</h2>

            </div>

            <div class="card-body">

                <pre style="white-space:pre-wrap;font-size:18px;">

{script}

                </pre>

                <hr>

                <a href="/project/{project_id}" class="btn btn-secondary">

                    ⬅ Back

                </a>

            </div>

        </div>

    </div>

    </body>

    </html>
    """)
