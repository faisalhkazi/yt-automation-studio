import json

from services.storage_service import StorageService


class ScenePreviewService:

    @staticmethod
    def load(project_id: int):

        scene_file = (
            StorageService.project_dir(project_id)
            / "scenes.json"
        )

        if not scene_file.exists():
            return []

        with open(scene_file, encoding="utf-8") as f:
            return json.load(f)
