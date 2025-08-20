1)  File Parser CRUD API with Progress Tracking
Overview

This project is a backend API that allows users to upload files (CSV, Excel, PDF), parse them, and manage their parsed data. It includes CRUD operations for files and extracted content, and a progress tracking system so users can check parsing status in real time.

Features

* Upload files (CSV, Excel, PDF)

* Parse data and store in database

* Track parsing progress (Pending → In Progress → Completed)

* CRUD operations for files

* Asynchronous background parsing

Tech Stack

* Backend Framework: FastAPI (Python)

* Database: SQLite with SQLAlchemy ORM

* Validation: Pydantic

* File Handling: FastAPI UploadFile

* Background Processing: FastAPI BackgroundTasks




2)  Setup Instructions
1. Clone Repository
git clone <repo-url>
cd <project-folder>

2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Run the Server
uvicorn app.main:app --reload


API will run at: http://127.0.0.1:8000




3)  API Documentation
1. Upload File

POST /upload
Upload a file (CSV, Excel, PDF) for parsing.
Request (multipart/form-data):

file: <your_file>


Response:

{
  "file_id": 1,
  "filename": "data.csv",
  "status": "Pending"
}

2. Get All Files

GET /files
Returns all uploaded files.
Response:

[
  {
    "file_id": 1,
    "filename": "data.csv",
    "status": "Completed"
  }
]

3. Get File Progress

GET /files/{file_id}/progress
Returns parsing progress for a file.
Response:

{
  "file_id": 1,
  "progress": 75,
  "status": "In Progress"
}

4. Delete a File

DELETE /files/{file_id}
Deletes a file and its parsed data.
Response:

{
  "message": "File deleted successfully"
}

Sample Postman Collection

You need to create a Postman collection with the following endpoints:

POST /upload (with file upload)

GET /files

GET /files/{file_id}/progress

DELETE /files/{file_id}

After creating, Export the Postman Collection and add it to the repo as postman_collection.json.
