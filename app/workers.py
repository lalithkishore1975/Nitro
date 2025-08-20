import time
from sqlalchemy.orm import Session
from . import crud, utils

def process_file(db: Session, file_id: str, file_path: str):
    """
    Simulate background progress + parse file.
    """
    for i in range(0, 100, 20):
        crud.update_file_status(db, file_id, "processing", i)
        time.sleep(1)

    try:
        parsed_content = utils.parse_file(file_path)
        crud.save_parsed_content(db, file_id, parsed_content)
        crud.update_file_status(db, file_id, "ready", 100)
    except Exception as e:
        crud.update_file_status(db, file_id, "failed", 0)
