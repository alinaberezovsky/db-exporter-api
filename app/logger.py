from sqlalchemy import insert
from datetime import datetime
from app.db import get_engine
from app.models import export_log


def log_export(file_name: str, record_count: int, select_seconds: float, write_seconds: float): #Insert a single export execution record into the export_log table
    engine = get_engine()

    with engine.begin() as conn:
        conn.execute(
            insert(export_log).values(
                file_name=file_name,
                created_at=datetime.utcnow(),
                record_count=record_count,
                select_seconds=select_seconds,
                write_seconds=write_seconds,
            )
        )