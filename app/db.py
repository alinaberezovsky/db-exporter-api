from sqlalchemy import create_engine
from app.config import DATABASE_URL

def get_engine():
    if not DATABASE_URL:
        raise ValueError("DATABASE_URL is not set")
    return create_engine(DATABASE_URL)