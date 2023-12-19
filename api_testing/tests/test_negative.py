import requests

INVALID_ENDPOINT = "https://todo.pixegami.io/invalid"

def test_invalid_endpoint():
    response = requests.get(INVALID_ENDPOINT)
    assert response.status_code == 404
    pass

