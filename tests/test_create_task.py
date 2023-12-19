import requests
ENDPOINT_CREATE_TASK = "https://todo.pixegami.io"

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
