import os
import sys

from fastapi import FastAPI
import uvicorn

if __package__ in (None, ""):
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

from app.database import Base, engine
from app.models.users import User

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Hotel Booking API")


@app.get("/")
def home():
    return {"message": "Hotel Booking API is running successfully!"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
