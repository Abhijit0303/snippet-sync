# 🚀 SnippetSync API

A lightweight, enterprise-style FastAPI micro-SaaS for storing, searching, and managing code snippets.
Designed to be used daily by developers to save time and improve productivity.

---

## 📌 Features

- ✨ Store reusable code snippets
- 🔍 Search snippets by title, tag, or language
- 📝 Update snippets
- ❌ Delete snippets
- 🗄️ SQLAlchemy ORM + SQLite database
- 🧱 Clean architecture with:
  - Routers
  - Services
  - Repositories
  - Schemas (Pydantic v2)
  - Models
- 🔑 UUID-based snippet IDs
- ⚡ Super fast FastAPI backend
- 🧩 Easy to extend into full SaaS (auth, API keys, billing)

---

## 🧠 Problem This Solves

Developers waste time searching old code from:

- Notepad
- VSCode scratchpads
- Random gists
- Telegram saved messages
- Slack dumps

> ❗ SnippetSync acts as your **personal cloud snippet vault**
> accessible from anywhere via API.

---

## 🏗️ Project Structure

```
snippet-sync-api/
│
├── app/
│   ├── config.py
│   ├── database.py
│   ├── models/
│   │     └── snippet_model.py
│   ├── schemas/
│   │     └── snippet_schema.py
│   ├── repositories/
│   │     └── snippet_repository.py
│   ├── services/
│   │     └── snippet_service.py
│   ├── routers/
│   │     └── snippet_router.py
│   ├── utils/
│   │     └── id_generator.py
│   └── __init__.py
├── main.py
├── pyproject.toml
└── README.md
```

---

## 🛠️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Abhijit0303/snippet-sync
cd snippet-sync
```

### 2️⃣ Create virtual environment

```bash
uv venv .venv
source .venv/bin/activate   # Linux & Mac
.venv\Scripts\activate    # Windows
```

### 3️⃣ Install dependencies

```bash
uv sync
```

---

## ▶️ Running the Server

```bash
uv run uvicorn app.main:app --reload
```

Open API docs:
👉 http://127.0.0.1:8000/docs

---

## 📡 API Endpoints

### ✨ Create Snippet

**POST /snippets/add**

```json
{
  "title": "JWT Handler",
  "content": "def login(): pass",
  "language": "python",
  "tags": "auth,jwt"
}
```

---

### 🔍 Search Snippets

**GET /snippets/search**

Query params:

- title
- tag
- language

Example:

```
/snippets/search?tag=auth&language=python
```

---

### 📄 Get Snippet by ID

**GET /snippets/{id}**

---

### 📝 Update Snippet

**PUT /snippets/{id}**

```json
{
  "title": "Updated JWT Handler",
  "tags": "auth,updated"
}
```

---

### ❌ Delete Snippet

**DELETE /snippets/{id}**

---

## 🧱 Tech Stack

- **FastAPI** – REST framework
- **SQLAlchemy** – ORM
- **Pydantic v2** – validation
- **SQLite** – lightweight database
- **UUID** – snippet IDs

---

## 🚀 Future Roadmap

- 🔑 API Key Authentication
- 👥 User Accounts with JWT
- 💳 Stripe Billing Integration
- 🧩 Browser extension (Chrome)
- 💻 CLI tool to sync snippets
- ☁️ Deployment

---

## 🤝 Contributing

Pull requests are welcome.
For major changes, open an issue first.

---

## 📜 License

MIT License - Free to use and modify.

---

## ⭐ Support

If this project helps you, star the repo ⭐
and share it on X!
