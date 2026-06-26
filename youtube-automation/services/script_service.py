from pathlib import Path

from services.storage_service import StorageService
from services.logger import logger


class ScriptService:

    @staticmethod
    def save(project_id: int, script: str) -> Path:

        project_dir = StorageService.project_dir(project_id)

        filepath = project_dir / "script.txt"

        filepath.write_text(
            script,
            encoding="utf-8"
        )

        logger.info(f"Script saved : {filepath}")

        return filepath
