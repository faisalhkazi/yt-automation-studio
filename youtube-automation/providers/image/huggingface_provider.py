from pathlib import Path

from huggingface_hub import InferenceClient

from config import HF_TOKEN, HF_IMAGE_MODEL


class HuggingFaceImageProvider:

    client = InferenceClient(
        provider="hf-inference",
        api_key=HF_TOKEN,
    )

    @staticmethod
    def generate(output_file: Path, prompt: str):

        print(f"Generating {output_file.name}")

        image = HuggingFaceImageProvider.client.text_to_image(
            prompt=prompt,
            model=HF_IMAGE_MODEL,
        )

        image.save(output_file)
