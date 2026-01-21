from sqlalchemy.orm import Session
from app.models.snippet_models import Snippet
from app.schemas.snippet_schema import SnippetCreate, SnippetUpdate


class SnippetRepository:

    @staticmethod
    def create(db: Session, snippet_id: str, snippet: SnippetCreate) -> Snippet:
        db_snippet = Snippet(
            id = snippet_id,
            title=snippet.title,
            content=snippet.content,
            language=snippet.language,
            tags=snippet.tags
        )
        db.add(db_snippet)
        db.commit()
        db.refresh(db_snippet)
        return db_snippet

    @staticmethod
    def get_by_id(db: Session, snippet_id: str) -> Snippet:
        return db.query(Snippet).filter(Snippet.id == snippet_id).first()

    @staticmethod
    def search(db: Session, title: str, tag:str, language: str):
        query = db.query(Snippet)

        if title:
            query = query.filter(Snippet.title.contains(title))
        if tag:
            query = query.filter(Snippet.tags.contains(tag))
        if language:
            query = query.filter(Snippet.language == language)

        return query.all()

    @staticmethod
    def update(db: Session, snippet_id: str, data: SnippetUpdate):
        db_snippet = db.query(Snippet).filter(Snippet.id == snippet_id).first()
        if not db_snippet:
            return None

        updated_data = data.model_dump(exclude_unset=True)

        for key, value in updated_data.items():
            setattr(db_snippet, key, value)

        db.commit()
        db.refresh(db_snippet)
        return db_snippet

    @staticmethod
    def delete(db: Session, snippet_id: str) -> bool:
        db_snippet = db.query(Snippet).filter(Snippet.id == snippet_id).first()
        if not db_snippet:
            return False

        db.delete(db_snippet)
        db.commit()
        return True

