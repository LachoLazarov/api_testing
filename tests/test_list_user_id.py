import requests
import pytest
from logging import error, info

def test_list_tasks(api_endpoint, create_task):
    user_id = "test_user"

    # Create Task for Listing
    task_id = create_task(user_id, "Test Task for Listing")

    # List Tasks
    response = requests.get(f"{api_endpoint}/list-tasks/{user_id}")
    response.raise_for_status()
    assert response.status_code == 200, info('Error in listing tasks')
    error("Error in list_tasks")

    data = response.json()
    tasks = data.get("tasks", [])

    # Check if Tasks is a List
    assert isinstance(tasks, list), "Tasks should be a list"

# Additional info log to indicate the successful execution of the test
info("Test execution completed successfully.")