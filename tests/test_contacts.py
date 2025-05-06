# import pytest
# from fastapi.testclient import TestClient
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# from main import app
# from infrastructure.database.models import Base
# from infrastructure.database.session import SessionLocal

# # Test database setup
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:0000@localhost:5432/test_loan_db"
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# @pytest.fixture(scope="module")
# def test_db():
#     Base.metadata.create_all(bind=engine)
#     yield
#     Base.metadata.drop_all(bind=engine)

# @pytest.fixture
# def test_client(test_db):
#     def override_get_db():
#         try:
#             db = TestingSessionLocal()
#             yield db
#         finally:
#             db.close()
    
#     app.dependency_overrides[get_db] = override_get_db
#     yield TestClient(app)

# def test_create_contact(test_client):
#     response = test_client.post(
#         "/contacts/",
#         json={"name": "Test User", "email": "test@example.com", "phone": "1234567890"}
#     )
#     assert response.status_code == 200
#     data = response.json()
#     assert data["name"] == "Test User"
#     assert "id" in data

import requests
payload = {
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "1234567890"
}
response = requests.post("http://localhost:8000/contacts/", json=payload)
print(response.status_code)
print(response.text)