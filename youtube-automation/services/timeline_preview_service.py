import json

from services.storage_service import StorageService


class TimelinePreviewService:

    @staticmethod
    def load(project_id: int):

        project_dir = StorageService.project_dir(project_id)

        timeline_file = project_dir / "timeline.json"

        if not timeline_file.exists():
            return []

        return json.loads(
            timeline_file.read_text(
                encoding="utf-8"
            )
        )
