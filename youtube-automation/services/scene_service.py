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

        TARGET_WORDS = 140

        scenes = []

        current_scene = []
        current_words = 0

        scene_number = 1

        for paragraph in paragraphs:

            words = len(paragraph.split())

            current_scene.append(paragraph)

            current_words += words

            if current_words >= TARGET_WORDS:

                scenes.append({
                    "scene": scene_number,
                    "text": "\n\n".join(current_scene)
                })

                scene_number += 1

                current_scene = []

                current_words = 0

        # Save remaining paragraphs

        if current_scene:

            scenes.append({
                "scene": scene_number,
                "text": "\n\n".join(current_scene)
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
