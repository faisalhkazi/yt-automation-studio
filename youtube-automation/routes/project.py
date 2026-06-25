from fastapi import APIRouter

router = APIRouter()


@router.get("/project/{project_id}")
async def project(project_id: int):

    return {
        "project_id": project_id
    }
