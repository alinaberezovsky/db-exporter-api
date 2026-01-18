from sqlalchemy import Table, Column, Integer, String, Float, DateTime, MetaData
from datetime import datetime

metadata = MetaData()

export_log = Table(
    "export_log",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("file_name", String),
    Column("created_at", DateTime, default=datetime.utcnow),
    Column("record_count", Integer),
    Column("select_seconds", Float),
    Column("write_seconds", Float),
)