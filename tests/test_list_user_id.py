import requests
import pytest
import logging

def test_list_tasks(api_endpoint, create_task):
    user_id = "test_user"

    try:
        task_id = create_task(user_id, "Test Task for Listing")

        response = requests.get(f"{api_endpoint}/list-tasks/{user_id}")
        response.raise_for_status()
        assert response.status_code == 200

        data = response.json()
        tasks = data.get("tasks", [])
        assert isinstance(tasks, list)
    except Exception as e:
        logging.error(f"Error in test_list_tasks: {e}")
        raise
