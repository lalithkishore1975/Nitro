import pandas as pd
import json
from PyPDF2 import PdfReader

def parse_file(file_path: str) -> str:
    """
    Parse CSV, Excel, or PDF into structured JSON string.
    """
    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path)
        return df.to_json(orient="records")
    elif file_path.endswith(".xlsx"):
        df = pd.read_excel(file_path)
        return df.to_json(orient="records")
    elif file_path.endswith(".pdf"):
        reader = PdfReader(file_path)
        text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
        return json.dumps({"text": text})
    else:
        return json.dumps({"message": "Unsupported file type"})
