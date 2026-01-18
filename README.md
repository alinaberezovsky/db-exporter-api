# DB Exporter REST API

Author: Alina Berezovsky  
Date: 18/01/2026

### Overview
This project is a standalone REST API application that:
- Connects to a database using a configurable connection string
- Executes arbitrary SQL SELECT queries
- Exports query results to CSV files on disk
- Logs execution metadata into a database table

The application is database-agnostic and can work with any database supported by SQLAlchemy.

--------------------------------------------------

### Features
- REST API built with FastAPI
- Generic database connectivity via DATABASE_URL
- CSV export of query results
- Execution logging (file name, timestamp, record count, execution time)
- Packaged as a standalone Windows executable (EXE)

--------------------------------------------------

### Running the Application

Run the executable file:
db_exporter_api.exe

The API will be available at:
http://127.0.0.1:8000

The application reads the database connection string from an environment variable.
Before running the application, update the ".env" file and set the DATABASE_URL value.

After starting the application, open the Swagger UI at:
http://127.0.0.1:8000/docs

To export data:
1. Open the POST /export endpoint
2. Click "Try it out"
3. Enter a SQL SELECT query in the "sql" field
4. Click "Execute"

The response will include execution metadata, and the CSV file
will be created in the output directory.
--------------------------------------------------

### Logging

Each export execution is logged into the export_log table with:
- File name
- Creation timestamp
- Record count
- SELECT execution time
- CSV write time

--------------------------------------------------

### Repository Structure

app/  
  __init__.py - Marks the app directory as a Python package  
  main.py - REST API layer and request orchestration  
  config.py - Environment and configuration handling  
  db.py - Database connection and engine creation  
  exporter.py - Query execution and CSV export logic  
  logger.py - Execution metadata logging  
  models.py - Database schema definitions  

dist/  
  db_exporter_api.exe - Standalone executable

run_server.py - Application entry point used to start the FastAPI server and build the executable  

.env - Local environment configuration