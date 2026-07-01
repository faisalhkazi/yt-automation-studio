from pathlib import Path

from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
    "https://www.googleapis.com/auth/youtube"
]

CREDENTIALS_FILE = "credentials.json"
TOKEN_FILE = "storage/youtube/token.json"


class YouTubeAuth:

    @staticmethod
    def authenticate():

        flow = InstalledAppFlow.from_client_secrets_file(
            CREDENTIALS_FILE,
            SCOPES
        )

        creds = flow.run_local_server(
            port=8080,
            open_browser=True
        )

        token_path = Path(TOKEN_FILE)

        token_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        token_path.write_text(
            creds.to_json()
        )

        print("\n")
        print("=" * 70)
        print("YouTube connected successfully!")
        print(f"Token saved to: {TOKEN_FILE}")
        print("=" * 70)
