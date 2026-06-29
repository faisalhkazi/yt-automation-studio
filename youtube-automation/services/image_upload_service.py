from pathlib import Path

from fastapi import UploadFile

from services.storage_service import StorageService
from services.project_service import ProjectService
from services.logger import logger


class ImageUploadService:

    @staticmethod
    def upload(project_id: int, files: list[UploadFile]):

        image_dir = (
                StorageService.project_dir(project_id)
                / "images"
                )

        image_dir.mkdir(exist_ok=True)

        # Delete previous images
        for image in image_dir.glob("*"):
            image.unlink()

        for index, file in enumerate(files, start=1):

            suffix = Path(file.filename).suffix.lower()

            filename = f"scene_{index:03}{suffix}"

            with open(image_dir / filename, "wb") as f:
                f.write(file.file.read())

        ProjectService.update_images(
                project_id,
                image_dir.relative_to(image_dir.parents[2]).as_posix()
                )

        logger.info(f"{len(files)} images uploaded.")

    @staticmethod
    def count(project_id: int):

        image_dir = (
                StorageService.project_dir(project_id)
                / "images"
                )

        if not image_dir.exists():
            return 0

        return len(
                list(image_dir.glob("*.png")) +
                list(image_dir.glob("*.jpg")) +
                list(image_dir.glob("*.jpeg")) +
                list(image_dir.glob("*.webp"))
                )

    @staticmethod
    def replace(
            project_id: int,
            scene: int,
            image: UploadFile
            ):

        image_dir = (
                StorageService.project_dir(project_id)
                / "images"
                )

        image_dir.mkdir(exist_ok=True)

        # Delete old image for this scene
        for file in image_dir.glob(f"scene_{scene:03}.*"):
            file.unlink()

        suffix = Path(image.filename).suffix.lower()

        filename = f"scene_{scene:03}{suffix}"

        with open(image_dir / filename, "wb") as f:
            f.write(image.file.read())

        logger.info(f"Scene {scene} image replaced.")
