from sqlalchemy.orm import Session
from app.schemas.snippet_schema import SnippetCreate
from app.utils.id_generator import generate_uid
from app.repositories.snippet_repository import SnippetRepository


class SnippetService:

    @staticmethod
    def create_snippet(db: Session, snippet: SnippetCreate):
        snippet_id = generate_uid()
        return SnippetRepository.create(db, snippet_id, snippet)

    @staticmethod
    def get_snippet(db: Session, snippet_id: str):
        return SnippetRepository.get_by_id(db, snippet_id)

    @staticmethod
    def search_snippets(db: Session, title: str = "", tag: str = "", language: str = ""):
        return SnippetRepository.search(db, title, tag, language)

    @staticmethod
    def update_snippet(db: Session, snippet_id: str, data):
        return SnippetRepository.update(db, snippet_id, data)

    @staticmethod
    def delete_snippet(db: Session, snippet_id: str) -> bool:
        return SnippetRepository.delete(db, snippet_id)
