import subprocess
from pathlib import Path

from config import PIPER_BINARY, PIPER_MODEL
from services.logger import logger
from services.storage_service import StorageService


class PiperService:

    @staticmethod
    def generate(
        project_id: int,
        script_file: Path
    ):

        project_dir = StorageService.project_dir(project_id)

        output_file = project_dir / "audio.wav"

        command = [
            str(PIPER_BINARY),
            "--model",
            str(PIPER_MODEL),
            "--output_file",
            str(output_file),
        ]

        logger.info(
            f"Generating audio from {script_file.name}"
        )

        with open(script_file, "rb") as infile:

            subprocess.run(
                command,
                stdin=infile,
                check=True
            )

        logger.info(
            f"Audio generated : {output_file}"
        )

        return output_file
