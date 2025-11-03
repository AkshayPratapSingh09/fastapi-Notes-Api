# 🗒️ Notes API 

A production‑ready **note‑taking backend with version history**, built with FastAPI, SQLAlchemy ORM, Alembic migrations, and JWT authentication.

---

## 🚀 Features

- User registration & JWT login (hashed passwords)
- Full CRUD on notes
- Automatic versioning on every update
- Restore old versions easily
- PostgreSQL as DB with Alembic migrations
- Robust validation and fault tolerance
- Ready for Docker or Render/Neon deployment

---

## 🧩 Project Structure

```
app/
 ├── core/              # Config & security utilities
 ├── database/          # SQLAlchemy setup (sql_connect.py)
 ├── models/            # ORM models (User, Note, NoteVersion)
 ├── routers/           # FastAPI routers (auth, notes)
 ├── services/          # Business logic (users, notes)
 ├── schemas/           # Pydantic schemas
 └── main.py            # Entry point
alembic/                # Migration scripts
tests/                  # Pytest-based API tests
```

---

## ⚙️ Environment Variables

Create a `.env` file in project root:

```
DATABASE_URL=postgresql+psycopg://neondb_owner:npg_L5iyMZgrvD3H@ep-cool-king-ad3h4dry-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require
SECRET_KEY=change_me
ACCESS_TOKEN_EXPIRE_MINUTES=60
ALGORITHM=HS256
```

---

## 🧠 Local Setup

```bash
# Clone and activate venv
git clone <repo-url>
cd notes-api
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
alembic upgrade head

# Start server
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Visit → [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🌐 Production Deployment (Render / Railway / Docker)

**Render / Railway:**  
Set the environment variables from `.env` and define a start command:
```
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

**Docker (optional):**
```bash
docker build -t notes-api .
docker run -d -p 8000:8000 --env-file .env notes-api
```

---

## 📘 API Summary

| Endpoint | Method | Description | Auth |
|-----------|--------|-------------|------|
| `/auth/register` | POST | Register new user | ❌ |
| `/auth/login` | POST | Login to get JWT | ❌ |
| `/notes/` | POST | Create note | ✅ |
| `/notes/` | GET | List user notes | ✅ |
| `/notes/{id}` | GET | Fetch single note | ✅ |
| `/notes/{id}` | PATCH | Update note (creates new version) | ✅ |
| `/notes/{id}` | DELETE | Delete note | ✅ |
| `/notes/{id}/versions` | GET | List note versions | ✅ |
| `/notes/{id}/versions/{v}` | GET | Get specific version | ✅ |
| `/notes/{id}/versions/{v}/restore` | POST | Restore version | ✅ |

---

## 🧪 Testing

```bash
pytest -v
```

---

## 🌍 Deployment URL

**Production:** [https://notes-api.onrender.com](https://notes-api.onrender.com)

---

**Tagline:** _“Your notes evolve, your history stays.”_
