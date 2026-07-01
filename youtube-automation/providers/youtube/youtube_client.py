from pathlib import Path

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = [
    "https://www.googleapis.com/auth/youtube"
]

TOKEN_FILE = "storage/youtube/token.json"


class YouTubeClient:

    @staticmethod
    def connect():

        token_path = Path(TOKEN_FILE)

        if not token_path.exists():
            raise Exception(
                "YouTube account is not connected."
            )

        creds = Credentials.from_authorized_user_file(
            TOKEN_FILE,
            SCOPES
        )

        if creds.expired and creds.refresh_token:

            creds.refresh(Request())

            token_path.write_text(
                creds.to_json()
            )

        return build(
            "youtube",
            "v3",
            credentials=creds
        )
