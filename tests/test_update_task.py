import requests
import pytest
from data import ENDPOINT, ENDPOINT_CREATE_TASK, ENDPOINT_UPDATE_TASK
from logging import error, info

@pytest.fixture
def created_task():
    payload = {
        "content": "test-content",
        "user_id": "test_user_id",
        "is_done": False
    }
    create_task_response = requests.put(ENDPOINT_CREATE_TASK, json=payload)
    assert create_task_response.status_code == 200, \
        info('Error in creating task')
    error("Error in create_task")

    data = create_task_response.json()
    return data["task"]["task_id"]

def test_endpoint_create_task():
    payload = {
        "content": "test-content",
        "user_id": "test_user_id",
        "is_done": False
    }
    create_task_response = requests.put(ENDPOINT_CREATE_TASK, json=payload)
    assert create_task_response.status_code == 200, \
        info('Error in creating task')
    error("Error in create_task")

    data = create_task_response.json()
    task_id = data["task"]["task_id"]

    get_task_response = requests.get(ENDPOINT + f"/get-task/{task_id}")
    assert get_task_response.status_code == 200, \
        info('Error in getting task')
    error("Error in get_task")

    get_task_data = get_task_response.json()
    assert get_task_data["content"] == payload["content"], f"Content mismatch. Expected: {payload['content']}, Got: {get_task_data['content']}"
    assert get_task_data["user_id"] == payload["user_id"], f"User ID mismatch. Expected: {payload['user_id']}, Got: {get_task_data['user_id']}"

def test_can_update_task(created_task):
    new_payload = {
        "user_id": "test_user_id",
        "task_id": created_task,
        "content": "updated_content",
        "is_done": True
    }
    update_task_response = requests.put(ENDPOINT_UPDATE_TASK, json=new_payload)
    assert update_task_response.status_code == 200, \
        info('Error in updating task')
    error("Error in update_task")
