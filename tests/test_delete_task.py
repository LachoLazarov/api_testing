import requests
import pytest
from logging import error, info

def test_delete_task(api_endpoint, create_task):
    user_id = "test_user"
    task_id = create_task(user_id, "Test Task for Deletion")

    # Delete Task
    response = requests.delete(f"{api_endpoint}/delete-task/{task_id}")
    response.raise_for_status()
    assert response.status_code == 200, \
        info('Error in deleting task')
    error("Error in delete_task")

    # List Tasks
    list_response = requests.get(f"{api_endpoint}/list-tasks/{user_id}")
    list_response.raise_for_status()
    assert list_response.status_code == 200, \
        info('Error in listing tasks')
    error("Error in list_tasks")

    data = list_response.json()
    tasks = data.get("tasks", [])

    # Check if Task is Deleted
    assert isinstance(tasks, list), "Tasks should be a list"
    assert task_id not in [task.get("task_id") for task in tasks], f"Task with ID {task_id} still exists in the list"

# Additional info log to indicate the successful execution of the test
info("Test execution completed successfully.")
