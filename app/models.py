from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
from .database import Base

def generate_uuid():
    return str(uuid.uuid4())

class File(Base):
    __tablename__ = "files"

    id = Column(String, primary_key=True, index=True, default=generate_uuid)
    filename = Column(String, nullable=False)
    status = Column(String, default="uploading")
    progress = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

    content = relationship("FileContent", back_populates="file", cascade="all, delete")

class FileContent(Base):
    __tablename__ = "file_contents"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    file_id = Column(String, ForeignKey("files.id"))
    parsed_content = Column(Text)

    file = relationship("File", back_populates="content")
