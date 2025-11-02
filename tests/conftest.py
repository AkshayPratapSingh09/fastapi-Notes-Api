import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from app.main import app
from app.database.sql_connect import Base, get_db

TEST_URL = os.getenv("TEST_DATABASE_URL", "sqlite+pysqlite:///:memory:")
engine = create_engine(TEST_URL, connect_args={"check_same_thread": False} if TEST_URL.startswith("sqlite") else {})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

def override_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_db
client = TestClient(app)

@pytest.fixture
def http():
    return client
