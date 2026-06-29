import json

from services.storage_service import StorageService
from services.project_service import ProjectService
from services.logger import logger

from providers.image.huggingface_provider import HuggingFaceImageProvider



class ImageService:

    @staticmethod
    def generate(project_id: int):

        project_dir = StorageService.project_dir(project_id)

        prompt_file = project_dir / "prompts.json"

        image_dir = project_dir / "images"

        image_dir.mkdir(exist_ok=True)

        prompts = json.loads(
            prompt_file.read_text(encoding="utf-8")
        )

        for item in prompts:

            image_file = image_dir / f"scene_{item['scene']:03}.png"

            HuggingFaceImageProvider.generate(
                image_file,
                item["prompt"]
            )

        ProjectService.update_images(
            project_id,
            image_dir.relative_to(image_dir.parents[2]).as_posix()
        )

        logger.info(
            f"{len(prompts)} placeholder images generated."
        )

        return image_dir
