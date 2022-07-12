import pytest

from api2 import app


def test_app():
    response = app.test_client().get('/api/posts')
    assert response.status_code == 200


def test_app2():
    response1 = app.test_client().get('/api/posts/1')
    response2 = app.test_client().get('/api/posts/2')
    response3 = app.test_client().get('/api/posts/3')
    response4 = app.test_client().get('/api/posts/4')
    response100 = app.test_client().get('/api/posts/100')
    assert response1.status_code == 200
    assert response2.status_code == 200
    assert response3.status_code == 200
    assert response4.status_code == 200
    assert response100.status_code == 500
