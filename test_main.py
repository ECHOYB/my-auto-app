import pytest
from main_service import app  # <--- 重点：这里必须和你的文件名一致

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello AI" in response.data

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json()['status'] == "healthy"