from pathlib import Path
import base64

from openai import OpenAI

from config import OPENAI_API_KEY, IMAGE_MODEL


class OpenAIImageProvider:

    client = OpenAI(api_key=OPENAI_API_KEY)

    @staticmethod
    def generate(output_file: Path, prompt: str):

        print(f"Generating image: {output_file.name}")

        result = OpenAIImageProvider.client.images.generate(
            model=IMAGE_MODEL,
            prompt=prompt,
            size="1024x1024"
        )

        image_bytes = base64.b64decode(
            result.data[0].b64_json
        )

        output_file.write_bytes(image_bytes)
