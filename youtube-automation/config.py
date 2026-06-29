import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

PROJECT_ROOT = BASE_DIR.parent

STORAGE_DIR = BASE_DIR / "storage"

SCRIPT_DIR = STORAGE_DIR / "scripts"
AUDIO_DIR = STORAGE_DIR / "audio"
VIDEO_DIR = STORAGE_DIR / "videos"
IMAGE_DIR = STORAGE_DIR / "images"
SUBTITLE_DIR = STORAGE_DIR / "subtitles"
THUMBNAIL_DIR = STORAGE_DIR / "thumbnails"


PIPER_BINARY = PROJECT_ROOT / "piper" / "piper" / "piper"

PIPER_MODEL = PROJECT_ROOT / "piper" / "models" / "en_US-lessac-medium.onnx"

HF_TOKEN = os.getenv("HF_TOKEN")

HF_IMAGE_MODEL = "black-forest-labs/FLUX.1-dev"
