import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from app import create_app
from app.models import db, User, Task

@pytest.fixture
def client():
    # Set up test app
    app = create_app(testing=True)  # ensure you support testing=True in create_app
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["TESTING"] = True

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()

# ---------------------------
# User Tests
# ---------------------------
def test_create_user(client):
    res = client.post("/api/users/", json={
        "username": "hamdan",
        "email": "hamdan@example.com",
        "password": "secret"
    })
    assert res.status_code == 201
    data = res.get_json()
    assert "id" in data

def test_get_users(client):
    # create one user
    client.post("/api/users/", json={
        "username": "ali",
        "email": "ali@example.com",
        "password": "secret"
    })

    res = client.get("/api/users/")
    assert res.status_code == 200
    data = res.get_json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["username"] == "ali"

# ---------------------------
# Task Tests
# ---------------------------
def test_create_task(client):
    # First, create a user
    user_res = client.post("/api/users/", json={
        "username": "usman",
        "email": "usman@example.com",
        "password": "pass123"
    })
    user_id = user_res.get_json()["id"]

    # Now, create a task for that user
    res = client.post("/api/tasks/", json={
        "title": "Learn Flask",
        "description": "Build a REST API",
        "user_id": user_id
    })
    assert res.status_code == 201
    data = res.get_json()
    assert data["title"] == "Learn Flask"
    assert data["user_id"] == user_id

def test_get_tasks(client):
    # Create user
    user_res = client.post("/api/users/", json={
        "username": "fatima",
        "email": "fatima@example.com",
        "password": "123456"
    })
    user_id = user_res.get_json()["id"]

    # Create task
    client.post("/api/tasks/", json={
        "title": "Study Pytest",
        "description": "Write unit tests",
        "user_id": user_id
    })

    # Fetch tasks
    res = client.get("/api/tasks/")
    assert res.status_code == 200
    data = res.get_json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["title"] == "Study Pytest"
