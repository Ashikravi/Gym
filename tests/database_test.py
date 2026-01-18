from app.core.database_config import engine

try:
    with engine.connect() as connection:
        print("Connection successful! ✅")
except Exception as e:
    print(f"Failed to connect: {e}")
