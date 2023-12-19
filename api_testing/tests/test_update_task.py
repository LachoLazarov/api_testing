import requests
import pytest

ENDPOINT_CREATE_TASK = "https://todo.pixegami.io"

@pytest.fixture
def created_task():
    payload = {
        "content": "test-content",
        "user_id": "test_user_id",
        "is_done": False
    }
    create_task_response = requests.put(ENDPOINT_CREATE_TASK + "/create-task", json=payload)
    assert create_task_response.status_code == 200

    data = create_task_response.json()
    return data["task"]["task_id"]

def test_endpoint_create_task():
    payload = {
        "content": "test-content",
        "user_id": "test_user_id",
        "is_done": False
    }
    create_task_response = requests.put(ENDPOINT_CREATE_TASK + "/create-task", json=payload)
    assert create_task_response.status_code == 200

    data = create_task_response.json()
    task_id = data["task"]["task_id"]

    get_task_response = requests.get(ENDPOINT_CREATE_TASK + f"/get-task/{task_id}")
    assert get_task_response.status_code == 200

    get_task_data = get_task_response.json()
    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]

def test_can_update_task(created_task):
    new_payload = {
        "user_id": "test_user_id",
        "task_id": created_task,
        "content": "updated_content",
        "is_done": True
    }
    update_task_response = requests.put(ENDPOINT_CREATE_TASK + "/update-task", json=new_payload)
    assert update_task_response.status_code == 200
