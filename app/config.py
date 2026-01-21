import os

class Settings:
    PROJECT_NAME: str = "SnippetSync API"
    API_VERSION: str = "v1"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./snippets.db")

settings = Settings()
