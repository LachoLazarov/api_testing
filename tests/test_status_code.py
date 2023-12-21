import requests
ENDPOINT_STATUS_CODE = "https://todo.pixegami.io"


def test_endpoint_status_code():
    response = requests.get(ENDPOINT_STATUS_CODE)
    assert response.status_code == 200
    pass

