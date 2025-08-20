from sqlalchemy.orm import Session
from . import models

def create_file(db: Session, filename: str) -> models.File:
    db_file = models.File(filename=filename)
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return db_file

def update_file_status(db: Session, file_id: str, status: str, progress: int):
    file = db.query(models.File).filter(models.File.id == file_id).first()
    if file:
        file.status = status
        file.progress = progress
        db.commit()
        db.refresh(file)
    return file

def save_parsed_content(db: Session, file_id: str, content: str):
    file_content = models.FileContent(file_id=file_id, parsed_content=content)
    db.add(file_content)
    db.commit()
    db.refresh(file_content)
    return file_content

def get_file(db: Session, file_id: str):
    return db.query(models.File).filter(models.File.id == file_id).first()

def get_file_content(db: Session, file_id: str):
    return db.query(models.FileContent).filter(models.FileContent.file_id == file_id).first()

def list_files(db: Session):
    return db.query(models.File).all()

def delete_file(db: Session, file_id: str):
    file = db.query(models.File).filter(models.File.id == file_id).first()
    if file:
        db.delete(file)
        db.commit()
        return True
    return False
