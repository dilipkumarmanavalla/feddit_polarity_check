"""
UnitTest cases for polarity_check
"""

from fastapi.testclient import TestClient
import sys
import os

app_module_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app'))
sys.path.append(app_module_dir)

from app import main
import requests

client = TestClient(main.app)


def test_health_check():
    """
    Test case to check the health_check endpoint.
    """
    response = client.get("/health_check")
    assert response.status_code == 200
    data = response.json()
    assert data["Status"] == "Up"


def test_analyse_and_generate_polarity():
    """
    Test case to check the analyse_and_generate_polarity function.
    """
    comments = [
        {"id": 1, "username": "user1", "text": "positive comment", "created_at": "20240425100000"},
        {"id": 2, "username": "user2", "text": "negative comment", "created_at": "20240425T110000"}
    ]
    updated_comments = main.analyse_and_generate_polarity(comments)
    assert len(updated_comments) == 2
    assert updated_comments[0]["polarity_score"] == 1
    assert updated_comments[0]["polarity"] == "positive"
    assert updated_comments[1]["polarity_score"] == 0
    assert updated_comments[1]["polarity"] == "negative"


def test_get_comments():
    """
    Test case to check the get_comments endpoint.
    """
    hosts = ['0.0.0.0', 'localhost', 'feddit']
    for each_host in hosts:
        feddit_url = f"http://{each_host}:8080/api/v1"
        try:
            response = requests.get(feddit_url)
        except:
            class T:status_code = 500
            response = T
        if response.status_code == 200:
            main.FEDDIT_URL = f"http://{each_host}:8080"
            response = client.get("/comments", params={"subfeddit_id": "1"})
            assert response.status_code == 200
            data = response.json()
            assert "comments" in data
            assert len(data["comments"]) == 25
            continue

    main.FEDDIT_URL = "http://test_500:8080/api/v1"
    response = client.get("/comments", params={"subfeddit_id": "1"})
    assert response.status_code == 500
    print('server is not available')
