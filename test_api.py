import requests
import pytest
import os

SERVER_IP = os.getenv("SERVER_IP", "47.116.209.164")
BASE_URL = f"http://{SERVER_IP}:8080"

def test_health_check():
    res = requests.get(f"{BASE_URL}/health", timeout=10)
    assert res.status_code == 200
    assert res.json()["status"] == "ok"

def test_business_api():
    res = requests.get(f"{BASE_URL}/api/test", timeout=10)
    assert res.status_code == 200
    assert "通过" in res.text

if __name__ == '__main__':
    pytest.main(["-v", "--alluredir=allure-results"])
