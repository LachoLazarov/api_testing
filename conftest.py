import pytest
import requests
import logging


logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

@pytest.fixture
def api_endpoint():
    return "https://todo.pixegami.io/"

@pytest.fixture
def create_task(api_endpoint):
    def _create_task(user_id, content):
        try:
            payload = {
                "content": content,
                "user_id": user_id,
                "is_done": False
            }
            response = requests.put(f"{api_endpoint}/create-task", json=payload)
            response.raise_for_status()
            assert response.status_code == 200
            return response.json()["task"]["task_id"]
        except Exception as e:
            # Log any exceptions
            logger.error(f"Error in create_task: {e}")
            raise

    return _create_task
