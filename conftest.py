import pytest
import requests
from logging import error, info #Wildcard import is not a good practice. Thats why I import here only 2 methods

@pytest.fixture
def api_endpoint():
    return "https://todo.pixegami.io/"

@pytest.fixture
def create_task(api_endpoint):
    def _create_task(user_id, content):
        payload = {
            "content": content,
            "user_id": user_id,
            "is_done": False
        }
        response = requests.put(f"{api_endpoint}/create-task", json=payload)
        response.raise_for_status()
        assert response.status_code == 200, \
            info('Erro in created task')
        error("Error in create_task")
        return response.json()["task"]["task_id"]
        
    return _create_task

def test_something(api_endpoint, create_task):
    task_id = create_task(user_id=1, content="Sample Task")
