import pytest
from portfolio.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to My Portfolio" in response.data


def test_submit_feedback(client):
    response = client.post('/feedback', data={'name': 'John Doe', 'email': 'johndoe@example.com', 'feedback': 'Test feedback'})
    assert response.status_code == 200
    assert b"Thank you for your feedback!" in response.data


def test_report_page(client):
    response = client.get('/report')
    assert response.status_code == 200
    # Add assertions to check the content of the report page


if __name__ == '__main__':
    pytest.main()
