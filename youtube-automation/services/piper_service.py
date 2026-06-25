import subprocess
from pathlib import Path

from config import AUDIO_DIR, PIPER_BINARY, PIPER_MODEL
from services.logger import logger


class PiperService:

    @staticmethod
    def generate(script_file: Path):

        AUDIO_DIR.mkdir(parents=True, exist_ok=True)

        output_file = AUDIO_DIR / f"{script_file.stem}.wav"

        command = [
            PIPER_BINARY,
            "--model",
            PIPER_MODEL,
            "--output_file",
            str(output_file),
        ]

        logger.info(f"Generating audio from {script_file.name}")

        with open(script_file, "rb") as infile:
            subprocess.run(
                command,
                stdin=infile,
                check=True,
            )

        logger.info(f"Audio generated: {output_file.name}")

        return output_file
