# CRM Data Manager

## Project Overview
A Python-based employee data management
application integrated with PostgreSQL,
designed to demonstrate database management,
data validation, and CRUD operations.

## Features
- Create, retrieve, update, and delete records
- Case-insensitive employee search
- Duplicate record detection
- Data validation and exception handling
- Dynamic SQL queries
- Secure database credential management
- Interactive command-line interface

## Technology Stack
- Python
- PostgreSQL
- Psycopg 3
- Python-dotenv
- Git and GitHub

## Project Architecture
- main.py: Application logic and user interaction
- database.py: Database connectivity and SQL operations
- schema.sql: Database schema
- requirements.txt: Python dependencies
- .env.example: Environment configuration template

## Installation
1. Clone the repository.
2. Create and activate a virtual environment.
3. Run pip install -r requirements.txt.
4. Create a PostgreSQL database and execute schema.sql.
5. Copy .env.example to .env and configure credentials.
6. Run python main.py.

## Windows Troubleshooting
If Psycopg cannot load its binary library, use an
authorized local PostgreSQL installation.

For PostgreSQL 18, run in PowerShell:

$env:Path = "C:\Program Files\PostgreSQL\18\bin;$env:Path"
$env:PSYCOPG_IMPL = "python"

Adjust the path to your PostgreSQL installation.

## Future Enhancements
- Automated ETL pipelines
- CSV and Excel data integration
- Data transformation using Pandas
- REST API integration
- Web-based interface