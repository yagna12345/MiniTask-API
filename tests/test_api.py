import pytest
from fastapi.testclient import TestClient
from app.main import app, TASKS

@pytest.fixture(autouse=True)
def clear_tasks():
    TASKS.clear()
    yield
    TASKS.clear()

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_empty_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == {"tasks": []}

def test_create_task():
    response = client.post("/tasks", json={"title": "Learn Docker"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "title": "Learn Docker", "done": False}

def test_created_task_can_be_listed():
    client.post("/tasks", json={"title": "Build CI pipeline"})
    response = client.get("/tasks")
    assert len(response.json()["tasks"]) == 1
    assert response.json()["tasks"][0]["title"] == "Build CI pipeline"

def test_short_title_is_rejected():
    response = client.post("/tasks", json={"title": "No"})
    assert response.status_code == 422
