from pydantic import BaseModel
from datetime import datetime

class FileResponse(BaseModel):
    id: str
    filename: str
    status: str
    progress: int
    created_at: datetime

    class Config:
        from_attributes = True  

class FileProgress(BaseModel):
    file_id: str
    status: str
    progress: int

class ParsedContent(BaseModel):
    file_id: str
    parsed_content: str
