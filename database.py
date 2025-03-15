import sqlite3
import os

DB_FILE = "user_progress.db"

class UserProgressDB:
    def __init__(self):
        """Initialize database and create table if not exists."""
        self.conn = sqlite3.connect(DB_FILE, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS progress (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                category TEXT,
                scenario TEXT,
                user_response TEXT,
                feedback TEXT,
                score INTEGER,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()

    def save_progress(self, username, category, scenario, user_response, feedback, score):
        """Save user response, feedback, and score into the database."""
        self.cursor.execute("""
            INSERT INTO progress (username, category, scenario, user_response, feedback, score)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (username, category, scenario, user_response, feedback, score))
        self.conn.commit()

    def get_user_progress(self, username):
        """Retrieve all stored progress for a specific user, ordered by latest first."""
        self.cursor.execute("""
            SELECT timestamp, category, scenario, score FROM progress 
            WHERE username = ? 
            ORDER BY timestamp DESC
        """, (username,))
        return self.cursor.fetchall()

    def get_leaderboard(self, top_n=5):
        """Retrieve the top users based on their average scores."""
        self.cursor.execute("""
            SELECT username, AVG(score) as avg_score FROM progress 
            GROUP BY username 
            ORDER BY avg_score DESC 
            LIMIT ?
        """, (top_n,))
        return self.cursor.fetchall()

    def delete_user_progress(self, username):
        """Delete all progress data for a specific user."""
        self.cursor.execute("DELETE FROM progress WHERE username = ?", (username,))
        self.conn.commit()
        return f"All progress for {username} has been deleted."

progress_db = UserProgressDB()
