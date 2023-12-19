import requests
import pytest
import logging


def test_delete_task(api_endpoint, create_task):
    user_id = "test_user"
    task_id = create_task(user_id, "Test Task for Deletion")

    try:
        response = requests.delete(f"{api_endpoint}/delete-task/{task_id}")
        response.raise_for_status()
        assert response.status_code == 200

        list_response = requests.get(f"{api_endpoint}/list-tasks/{user_id}")
        list_response.raise_for_status()
        assert list_response.status_code == 200

        data = list_response.json()
        tasks = data.get("tasks", [])
        assert isinstance(tasks, list)
        assert task_id not in [task.get("task_id") for task in tasks]
    except Exception as e:
        logging.error(f"Error in test_delete_task: {e}")
        raise
