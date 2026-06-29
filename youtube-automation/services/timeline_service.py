import json
from pathlib import Path
from services.storage_service import StorageService
from services.project_service import ProjectService


class TimelineService:
        

    @staticmethod
    def generate(project_id: int):

        project_dir = StorageService.project_dir(project_id)

        scenes = json.loads(
                (project_dir / "scenes.json").read_text(
                    encoding="utf-8"
                    )
                )

        timeline = []

        for scene in scenes:

            image_file = None

            for ext in ["png", "jpg", "jpeg", "webp"]:

                candidate = (
                        project_dir
                        / "images"
                        / f"scene_{scene['scene']:03}.{ext}"
                        )

                if candidate.exists():
                    image_file = candidate.name
                    break

            timeline.append({
                "scene": scene["scene"],
                "image": f"images/{image_file}",
                "duration": round(scene.get("duration", 0), 2),
                "text": scene["text"]
                })

        timeline_file = project_dir / "timeline.json"

        timeline_file.write_text(
                json.dumps(
                    timeline,
                    indent=4,
                    ensure_ascii=False
                    ),
                encoding="utf-8"
                )

        ProjectService.update_timeline(
                project_id,
                timeline_file.relative_to(
                    timeline_file.parents[2]
                    ).as_posix()
                )

        return timeline_file
