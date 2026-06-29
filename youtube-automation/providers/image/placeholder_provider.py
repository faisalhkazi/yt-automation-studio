from pathlib import Path

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class PlaceholderImageProvider:

    WIDTH = 1280
    HEIGHT = 720

    @staticmethod
    def generate(output_file: Path, text: str):

        image = Image.new(
            "RGB",
            (PlaceholderImageProvider.WIDTH,
             PlaceholderImageProvider.HEIGHT),
            "#202124"
        )

        draw = ImageDraw.Draw(image)

        try:
            title_font = ImageFont.truetype(
                "DejaVuSans-Bold.ttf",
                48
            )

            body_font = ImageFont.truetype(
                "DejaVuSans.ttf",
                28
            )

        except Exception:

            title_font = ImageFont.load_default()
            body_font = ImageFont.load_default()

        draw.text(
            (50, 40),
            "Scene Placeholder",
            fill="white",
            font=title_font
        )

        draw.text(
            (50, 140),
            text[:700],
            fill="#dddddd",
            font=body_font
        )

        image.save(output_file)
