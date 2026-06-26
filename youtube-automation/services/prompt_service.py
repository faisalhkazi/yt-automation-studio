import json

from services.logger import logger
from services.storage_service import StorageService
from services.project_service import ProjectService


class PromptService:

    @staticmethod
    def generate(project_id: int):

        project_dir = StorageService.project_dir(project_id)

        scene_file = project_dir / "scenes.json"

        prompt_file = project_dir / "prompts.json"

        scenes = json.loads(
            scene_file.read_text(encoding="utf-8")
        )

        prompts = []

        STYLE = (
            "Ultra realistic, cinematic, photorealistic, "
            "dramatic lighting, 16:9, 8K, highly detailed, "
            "professional photography."
        )

        for scene in scenes:

            prompts.append({

                "scene": scene["scene"],

                "text": scene["text"],

                "prompt": f"{STYLE} {scene['text']}"
            })

        prompt_file.write_text(
            json.dumps(
                prompts,
                indent=4,
                ensure_ascii=False
            ),
            encoding="utf-8"
        )

        ProjectService.update_prompt(
            project_id,
            prompt_file.relative_to(prompt_file.parents[2]).as_posix()
        )

        logger.info(f"{len(prompts)} prompts generated")

        return prompt_file
