import json
import wave

from services.logger import logger
from services.storage_service import StorageService
from services.project_service import ProjectService


class SceneService:

    @staticmethod
    def generate(project_id: int):

        project_dir = StorageService.project_dir(project_id)

        script_file = project_dir / "script.txt"
        scene_file = project_dir / "scenes.json"
        audio_file = project_dir / "audio.wav"

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

        # -------------------------
        # Build scenes
        # -------------------------

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

        if current_scene:

            scenes.append({
                "scene": scene_number,
                "text": "\n\n".join(current_scene)
            })

        # -------------------------
        # Calculate durations
        # -------------------------

        with wave.open(str(audio_file), "rb") as wav:
            audio_length = wav.getnframes() / wav.getframerate()

        total_words = sum(
            len(scene["text"].split())
            for scene in scenes
        )

        for scene in scenes:

            words = len(scene["text"].split())

            scene["duration"] = round(
                audio_length * words / total_words,
                2
            )

        # -------------------------
        # Save
        # -------------------------

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

    @staticmethod
    def count(project_id: int):

        project_dir = StorageService.project_dir(project_id)

        scene_file = project_dir / "scenes.json"

        if not scene_file.exists():
            return 0

        scenes = json.loads(
            scene_file.read_text(encoding="utf-8")
        )

        return len(scenes)
