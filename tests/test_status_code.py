import requests
import pytest
from data import ENDPOINT, INVALID_ENDPOINT
from logging import error, info

def test_endpoint_status_code():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200, \
        info(f"Successfully retrieved data from {ENDPOINT}")
    error(f"Failed to retrieve data from {ENDPOINT}. Response code: {response.status_code}")

def test_invalid_endpoint():
    response = requests.get(INVALID_ENDPOINT)
    assert response.status_code == 404, \
        info("Successfully handled invalid endpoint")
    error(f"Expected status code 404 for invalid endpoint. Got: {response.status_code}")
