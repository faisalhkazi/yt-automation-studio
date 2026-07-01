from pathlib import Path

from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
    "https://www.googleapis.com/auth/youtube"
]

CREDENTIALS_FILE = "credentials.json"

TOKEN_FILE = "storage/youtube/token.json"


class OAuthService:

    @staticmethod
    def get_authorization_url():

        flow = InstalledAppFlow.from_client_secrets_file(
            CREDENTIALS_FILE,
            SCOPES
        )

        auth_url, _ = flow.authorization_url(
            access_type="offline",
            prompt="consent"
        )

        Path("storage/youtube").mkdir(
            parents=True,
            exist_ok=True
        )

        (Path("storage/youtube") / "flow.pkl").write_bytes(
            flow.__getstate__().__repr__().encode()
        )

        return auth_url
