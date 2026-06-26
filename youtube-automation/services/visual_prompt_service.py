import json

from services.logger import logger
from services.storage_service import StorageService
from services.project_service import ProjectService


class VisualPromptService:

    STYLE = (
        "Ultra realistic, cinematic, dramatic lighting, "
        "8K, 16:9, highly detailed, professional photography."
    )

    @staticmethod
    def generate(project_id: int):

        project_dir = StorageService.project_dir(project_id)

        prompts_file = project_dir / "prompts.json"

        output_file = project_dir / "visual_prompts.json"

        prompts = json.loads(
            prompts_file.read_text(encoding="utf-8")
        )

        visual_prompts = []

        for item in prompts:

            visual_prompts.append({

                "scene": item["scene"],

                "prompt":
                    f"{VisualPromptService.STYLE} "
                    f"{item['text'][:250]}"
            })

        output_file.write_text(
            json.dumps(
                visual_prompts,
                indent=4,
                ensure_ascii=False
            ),
            encoding="utf-8"
        )

        ProjectService.update_visual_prompt(
            project_id,
            output_file.relative_to(output_file.parents[2]).as_posix()
        )

        logger.info(
            f"{len(visual_prompts)} visual prompts generated"
        )

        return output_file
