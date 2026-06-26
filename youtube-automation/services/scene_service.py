import json

from services.logger import logger
from services.storage_service import StorageService
from services.project_service import ProjectService

class SceneService:

    @staticmethod
    def generate(project_id: int):
        
        project_dir = StorageService.project_dir(project_id)

        script_file = project_dir / "script.txt"

        scene_file = project_dir / "scenes.json"

        text = script_file.read_text(encoding="utf-8")

        paragraphs = [
            p.strip()
            for p in text.split("\n")
            if p.strip()
        ]

        scenes = []

        for index, paragraph in enumerate(paragraphs, start=1):

            scenes.append({
                "scene": index,
                "text": paragraph
            })

        scene_file.write_text(
            json.dumps(
                scenes,
                indent=4,
                ensure_ascii=False
            ),
            encoding="utf-8"
        )

        ProjectService.update_scene(
        project_id,
        scene_file.relative_to(scene_file.parents[2]).as_posix()
        )

        logger.info(f"{len(scenes)} scenes generated")



        return scene_file
