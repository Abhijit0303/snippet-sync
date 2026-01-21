from fastapi import FastAPI
from app.database import Base, engine
from app.routers.snippet_router import router as snippet_router


Base.metadata.create_all(bind=engine)

app = FastAPI(title="SnippetSync API", version="v1")

app.include_router(snippet_router)

@app.get("/")
def root():
    return {"message": "SnippetSync API is running 🚀"}
