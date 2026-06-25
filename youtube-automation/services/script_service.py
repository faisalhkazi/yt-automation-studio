from datetime import datetime
from pathlib import Path

from config import SCRIPT_DIR
from services.logger import logger


class ScriptService:

    @staticmethod
    def save(script: str):

        SCRIPT_DIR.mkdir(parents=True, exist_ok=True)

        filename = datetime.now().strftime("%Y%m%d_%H%M%S")

        filepath = SCRIPT_DIR / f"{filename}.txt"

        filepath.write_text(script, encoding="utf-8")

        logger.info(f"Script saved : {filepath}")

        return filepath
