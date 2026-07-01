from providers.youtube.youtube_client import YouTubeClient


class YouTubeService:

    @staticmethod
    def authorization_url():

        return YouTubeClient.authorization_url()
