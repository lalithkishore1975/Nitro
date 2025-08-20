File Parser CRUD API with Progress Tracking
Overview

This project is a backend API that allows users to upload files, parse them, and manage parsed data. It includes CRUD operations for files and their content and also provides a progress tracking system so users can check the status of parsing in real-time.

The main goal of this project is to handle different file types (CSV, PDF, Excel) and extract data without blocking the main thread using asynchronous processing.

Features

File upload API (supports CSV, Excel, and PDF)

Parse uploaded files and store extracted content

Track parsing progress and status (Pending, In Progress, Completed)

CRUD operations for file metadata and parsed data

Asynchronous background processing for scalability

Tech Stack

Framework: FastAPI (Python)

Database: SQLite (for simplicity) using SQLAlchemy ORM

Data Validation: Pydantic

File Handling: FastAPI UploadFile

Background Processing: FastAPI BackgroundTasks

API Endpoints
Upload a file
POST /upload

Uploads a file for parsing.

Get progress of a file
GET /files/{file_id}/progress

Returns the parsing status and progress percentage.

Get all files
GET /files

Returns all uploaded files with status.

Delete a file
DELETE /files/{file_id}

Deletes a file and its parsed data.

How Progress Tracking Works

When a file is uploaded, its status is Pending.

A background task starts parsing the file asynchronously.

While parsing, progress (in %) is updated in the database.

Users can check progress using the /files/{file_id}/progress endpoint.

Setup & Run

Clone the project

git clone <repo-url>
cd project-folder

Create and activate virtual environment

python -m venv venv
source venv/bin/activate # For Linux/Mac
venv\Scripts\activate # For Windows

Install dependencies

pip install -r requirements.txt

Run the application

uvicorn app.main:app --reload

Access API

Base URL: http://127.0.0.1:8000

Swagger UI (for testing): /docs
