Setup
1) python -m venv .venv && source .venv/bin/activate
2) pip install -r requirements.txt
3) export SECRET_KEY="your_secret"
4) export DATABASE_URL="postgresql+psycopg://neondb_owner:npg_L5iyMZgrvD3H@ep-cool-king-ad3h4dry-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
5) alembic upgrade head
6) uvicorn app.main:app --host 0.0.0.0 --port 8000

Auth
POST /auth/register {email,password}
POST /auth/login form-data username,password

Notes
POST /notes
GET /notes
GET /notes/{id}
PATCH /notes/{id}
DELETE /notes/{id}

Versions
GET /notes/{id}/versions
GET /notes/{id}/versions/{v}
POST /notes/{id}/versions/{v}/restore
