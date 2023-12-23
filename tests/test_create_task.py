import requests
from data import ENDPOINT_CREATE_TASK, ENDPOINT_GET_TASK
from logging import error, info

def test_endpoint_create_task():
    payload = {
        "content": "test-content",
        "user_id": "test_user_id",
        "is_done": False
    }

    # Create Task
    create_task_response = requests.put(ENDPOINT_CREATE_TASK, json=payload)
    assert create_task_response.status_code == 200, \
        info('Error in created task')
    error("Error in create_task")

    data = create_task_response.json()
    task_id = data["task"]["task_id"]

    # Get Task
    get_task_response = requests.get(ENDPOINT_GET_TASK + f"/{task_id}")
    assert get_task_response.status_code == 200, \
        info('Error in getting task')
    error("Error in get_task")

    get_task_data = get_task_response.json()

    # Check Content
    assert get_task_data["content"] == payload["content"], f"Content mismatch. Expected: {payload['content']}, Got: {get_task_data['content']}"

    # Check User ID
    assert get_task_data["user_id"] == payload["user_id"], f"User ID mismatch. Expected: {payload['user_id']}, Got: {get_task_data['user_id']}"

# Additional info log to indicate the successful execution of the test
info("Test execution completed successfully.")
