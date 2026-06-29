from services.project_service import ProjectService
from services.scene_service import SceneService
from services.image_upload_service import ImageUploadService


class WorkflowService:

    @staticmethod
    def status(project_id: int):

        project = ProjectService.get(project_id)

        scene_count = SceneService.count(project_id)
        image_count = ImageUploadService.count(project_id)

        return {
            "audio_ready": bool(project["audio_file"]),
            "scene_ready": bool(project["scene_file"]),
            "scene_count": scene_count,
            "image_count": image_count,
            "timeline_ready": bool(project["timeline_file"]),
            "video_ready": bool(project["video_file"]),
            "images_complete": (
                scene_count > 0 and image_count >= scene_count
            )
        }
