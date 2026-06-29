import subprocess
from pathlib import Path


class FFmpegRenderer:

    @staticmethod
    def render_scene(
        image: Path,
        duration: float,
        output: Path
    ):

        command = [

            "ffmpeg",

            "-y",

            "-loop",
            "1",

            "-i",
            str(image),

            "-t",
            f"{duration:.2f}",

            "-r",
            "25",

            "-vf",
            
            "scale=1920:1080:force_original_aspect_ratio=increase,"
            "crop=1920:1080,"
            "zoompan=z='min(zoom+0.0005,1.15)':"
            "x='iw/2-(iw/zoom/2)':"
            "y='ih/2-(ih/zoom/2)':"
            "d=25*{:.2f}".format(duration),


            "-c:v",
            "libx264",

            "-pix_fmt",
            "yuv420p",

            str(output)

        ]

        subprocess.run(
            command,
            check=True
        )

    @staticmethod
    def concat(render_dir: Path):

        concat_file = render_dir / "videos.txt"

        videos = sorted(render_dir.glob("scene_*.mp4"))

        with open(concat_file, "w") as f:
            for video in videos:
                f.write(f"file '{video.resolve()}'\n")

        slideshow = render_dir / "slideshow.mp4"

        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-f",
                "concat",
                "-safe",
                "0",
                "-i",
                str(concat_file),
                "-c",
                "copy",
                str(slideshow),
            ],
            check=True,
        )

        return slideshow


    @staticmethod
    def merge_audio(
        slideshow: Path,
        audio: Path,
        output: Path,
    ):

        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-i",
                str(slideshow),
                "-i",
                str(audio),
                "-c:v",
                "copy",
                "-c:a",
                "aac",
                "-shortest",
                str(output),
            ],
            check=True,
        )
