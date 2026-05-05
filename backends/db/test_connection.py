from sqlalchemy import text
from backends.db.session import engine

def test_connection():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            print("✅ Database connected successfully:", result.scalar())
    except Exception as e:
        print("❌ Database connection failed:", e)


if __name__ == "__main__":
    test_connection()