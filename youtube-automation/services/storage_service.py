from pathlib import Path

from config import STORAGE_DIR


class StorageService:

    @staticmethod
    def project_dir(project_id: int) -> Path:

        folder = STORAGE_DIR / f"project_{project_id}"

        folder.mkdir(
            parents=True,
            exist_ok=True
        )

        return folder
    @staticmethod
    def project_file(project_id: int, filename: str):

        return StorageService.project_dir(project_id) / filename
