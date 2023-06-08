import pytest
from portfolio.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to My Portfolio" in response.data

def test_submit_feedback(client):
    response = client.post('/feedback', data={
        'name': 'John Doe',
        'email': 'john@example.com',
        'feedback': 'Test feedback'
    })
    assert response.status_code == 200
    assert b"Thank you for your feedback!" in response.data

def test_report_page(client):
    response = client.get('/report')
    assert response.status_code == 200
    assert b"Total Visitors:" in response.data
    # Add more assertions as needed for the report page

# Add more test cases as needed

if __name__ == '__main__':
    pytest.main()
