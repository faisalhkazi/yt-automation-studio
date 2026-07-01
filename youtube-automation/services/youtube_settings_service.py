from services.database_service import DatabaseService


class YouTubeSettingsService:

    @staticmethod
    def get():

        conn = DatabaseService.connect()

        conn.row_factory = __import__("sqlite3").Row

        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM youtube_settings
            LIMIT 1
        """)

        settings = cursor.fetchone()

        conn.close()

        return settings
