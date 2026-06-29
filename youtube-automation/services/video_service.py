import json

from providers.video.ffmpeg_renderer import FFmpegRenderer

from services.storage_service import StorageService

from services.project_service import ProjectService

class VideoService:

    @staticmethod
    def generate(project_id: int):

        project_dir = StorageService.project_dir(project_id)

        render_dir = StorageService.render_dir(project_id)

        timeline = json.loads(
            (project_dir / "timeline.json").read_text()
        )

        for scene in timeline:

            image = project_dir / scene["image"]
            
            duration = scene["duration"]


            output = (
                render_dir /
                f"scene_{scene['scene']:03}.mp4"
            )

            FFmpegRenderer.render_scene(

                image,

                duration,

                output

            )

        slideshow = FFmpegRenderer.concat(render_dir)

        final_video = project_dir / "video.mp4"

        FFmpegRenderer.merge_audio(
            slideshow,
            project_dir / "audio.wav",
            final_video
            )

        ProjectService.update_video(
            project_id,
            final_video.relative_to(
                final_video.parents[2]
            ).as_posix()
        )

        return final_video

