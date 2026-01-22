from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.snippet_schema import SnippetResponse, SnippetCreate, SnippetUpdate
from app.services.snippet_service import SnippetService
from app.auth.dependency import get_current_user


router = APIRouter(prefix="/snippets", tags=["snippets"])

@router.get("/search")
def search_snippets(title: str = "", tag: str = "", language: str = "", db: Session = Depends(get_db)):
    snippets = SnippetService.search_snippets(db, title, tag, language)
    return snippets

@router.post("/add", response_model=SnippetResponse)
def create_snippet(data: SnippetCreate, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    snippet = SnippetService.create_snippet(db, data)
    return snippet

@router.get("/{snippet_id}", response_model=SnippetResponse)
def get_snippet(snippet_id: str, db: Session = Depends(get_db)):
    snippet = SnippetService.get_snippet(db, snippet_id)
    if not snippet:
        raise HTTPException(status_code=404, detail="Snippet not found")
    return snippet

@router.put("/{snippet_id}", response_model=SnippetResponse)
def update_snippet(snippet_id: str, data: SnippetUpdate, db: Session = Depends(get_db)):
    snippet = SnippetService.update_snippet(db, snippet_id, data)
    if not snippet:
        raise HTTPException(status_code=404, detail="Snippet not found")
    return snippet


@router.delete("/{snippet_id}")
def delete_snippet(snippet_id: str, db: Session = Depends(get_db)):
    success = SnippetService.delete_snippet(db, snippet_id)
    if not success:
        raise HTTPException(status_code=404, detail="Snippet not found")
    return {"status": "success", "detail": "Snippet deleted successfully"}


