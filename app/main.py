from fastapi import FastAPI, HTTPException
from sqlalchemy import text
from app.db import get_engine
from app.exporter import export_to_csv
from app.logger import log_export
from app.models import metadata
import os

app = FastAPI()

@app.on_event("startup")
def create_tables_on_startup():
    engine = get_engine()
    metadata.create_all(engine)

@app.get("/health") #Health check endpoint (service status indicator)
def health():
    return {"status": "ok"}

@app.get("/db-check") #Database connectivity check
def db_check():
    try:
        engine = get_engine()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"DB connection failed: {e}")

    return {"db": "ok"}

@app.post("/export") #Execute a SQL SELECT query and export the results to a CSV file
def export(sql: str):
    try:
        os.makedirs("output", exist_ok=True) #Ensure output directory exists
        file_name = "export.csv"
        output_path = f"output/{file_name}"

        result = export_to_csv(sql_query=sql, output_file=output_path) #Execute query and export to CSV

        log_export( #Log execution metadata
            file_name=file_name,
            record_count=result["record_count"],
            select_seconds=result["select_seconds"],
            write_seconds=result["write_seconds"],
        )

        return {"file": output_path, **result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))