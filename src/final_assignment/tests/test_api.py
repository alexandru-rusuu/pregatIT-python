import sys
import os
from fastapi.testclient import TestClient

os.environ["DB_PASSWORD"] = "mysecretpassword"
os.environ["DB_HOST"] = "localhost"

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api import app

client = TestClient(app)
test_task_id = None

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_task():
    global test_task_id
    payload = {
        "title": "Task din Teste Automate",
        "owner": "Robot",
        "description": "Testam acoperirea codului"
    }
    response = client.post("/tasks", json=payload)

    assert response.status_code == 201
    data = response.json()

    assert data["title"] == "Task din Teste Automate"
    assert data["status"] == "CREATED"
    assert "id" in data

    test_task_id = data["id"]


def test_list_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0


def test_get_task_by_id():
    global test_task_id
    response = client.get(f"/tasks/{test_task_id}")
    assert response.status_code == 200
    assert response.json()["id"] == test_task_id


def test_update_task():
    global test_task_id
    payload = {"title": "Titlu Updatat"}
    response = client.patch(f"/tasks/{test_task_id}", json=payload)
    assert response.status_code == 200
    assert response.json()["title"] == "Titlu Updatat"


def test_change_status():
    global test_task_id
    payload = {"new_status": "IN_PROGRESS"}
    response = client.post(f"/tasks/{test_task_id}/status", json=payload)
    assert response.status_code == 200
    assert response.json()["status"] == "IN_PROGRESS"


def test_delete_task():
    global test_task_id
    response = client.delete(f"/tasks/{test_task_id}")
    assert response.status_code == 204


def test_get_deleted_task():
    global test_task_id
    response = client.get(f"/tasks/{test_task_id}")
    assert response.status_code == 404