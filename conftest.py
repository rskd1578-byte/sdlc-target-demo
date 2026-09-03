import pytest

from app import app as flask_app


@pytest.fixture
def client():
    """Standard Flask test client fixture available to all tests."""
    return flask_app.test_client()