import csv
import time
from sqlalchemy import text
from app.db import get_engine

def export_to_csv(sql_query: str, output_file: str): #Run a SQL SELECT query and export the result to a CSV file
    start_time = time.time() #Record start time


    engine = get_engine() #Create database engine using the configured DATABASE_URL

    select_start = time.time() #Measure SELECT time
    with engine.connect() as conn:
        result = conn.execute(text(sql_query))
        rows = result.fetchall()
        columns = result.keys()
    select_end = time.time()

    write_start = time.time() #Measure WRITE time
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(columns)
        writer.writerows(rows)
    write_end = time.time()

    return {
        "record_count": len(rows),
        "select_seconds": round(select_end - select_start, 3),
        "write_seconds": round(write_end - write_start, 3),
    }