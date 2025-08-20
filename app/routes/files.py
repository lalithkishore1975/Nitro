from fastapi import APIRouter, UploadFile, Depends, BackgroundTasks, HTTPException
import shutil, os
from sqlalchemy.orm import Session
from .. import database, crud, schemas, workers

router = APIRouter()
UPLOAD_DIR = "uploads"

@router.post("/", response_model=schemas.FileResponse)
def upload_file(file: UploadFile, background_tasks: BackgroundTasks, db: Session = Depends(database.get_db)):
    # Save metadata in DB
    db_file = crud.create_file(db, file.filename)

    # Save file locally
    file_path = os.path.join(UPLOAD_DIR, f"{db_file.id}_{file.filename}")
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Background task to process
    background_tasks.add_task(workers.process_file, db, db_file.id, file_path)

    return db_file

@router.get("/{file_id}/progress", response_model=schemas.FileProgress)
def get_progress(file_id: str, db: Session = Depends(database.get_db)):
    file = crud.get_file(db, file_id)
    if not file:
        raise HTTPException(status_code=404, detail="File not found")
    return {"file_id": file.id, "status": file.status, "progress": file.progress}

@router.get("/{file_id}")
def get_file_content(file_id: str, db: Session = Depends(database.get_db)):
    file = crud.get_file(db, file_id)
    if not file:
        raise HTTPException(status_code=404, detail="File not found")

    if file.status != "ready":
        return {"message": "File upload or processing in progress. Please try again later."}

    content = crud.get_file_content(db, file_id)
    return {"file_id": file.id, "parsed_content": content.parsed_content}

@router.get("/", response_model=list[schemas.FileResponse])
def list_files(db: Session = Depends(database.get_db)):
    return crud.list_files(db)

@router.delete("/{file_id}")
def delete_file(file_id: str, db: Session = Depends(database.get_db)):
    success = crud.delete_file(db, file_id)
    if not success:
        raise HTTPException(status_code=404, detail="File not found")
    return {"message": "File deleted successfully"}
