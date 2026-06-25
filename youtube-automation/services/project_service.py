from services.database_service import DatabaseService


class ProjectService:

    @staticmethod
    def initialize():

        conn = DatabaseService.connect()

        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            title TEXT,

            category TEXT,

            script TEXT,

            script_file TEXT,

            audio_file TEXT,

            video_file TEXT,

            thumbnail_file TEXT,

            status TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """)

        conn.commit()

        conn.close()
    

    @staticmethod
    def create(title: str, category: str, script: str):

        conn = DatabaseService.connect()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO projects
            (
                title,
                category,
                script,
                status
            )
            VALUES (?, ?, ?, ?)
        """, (
            title,
            category,
            script,
            "SCRIPT_RECEIVED"
        ))

        conn.commit()

        project_id = cursor.lastrowid

        conn.close()

        return project_id



    @staticmethod
    def update_script(project_id: int, script_file: str):

        conn = DatabaseService.connect()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE projects
            SET script_file = ?,
                status = ?
            WHERE id = ?
        """, (
            script_file,
            "SCRIPT_READY",
            project_id
        ))

        conn.commit()
        conn.close()


    @staticmethod
    def update_audio(project_id: int, audio_file: str):

        conn = DatabaseService.connect()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE projects
            SET audio_file = ?,
                status = ?
            WHERE id = ?
        """, (
            audio_file,
            "AUDIO_READY",
            project_id
        ))

        conn.commit()
        conn.close()


    @staticmethod
    def list_projects():

        conn = DatabaseService.connect()

        conn.row_factory = __import__("sqlite3").Row

        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM projects
            ORDER BY id DESC
        """)

        rows = cursor.fetchall()

        conn.close()

        return rows
