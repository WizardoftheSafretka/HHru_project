import pytest


@pytest.fixture()
def test_vacancy():
    return {
        "items": [{"name": "Developer"}, {"name": "Manager"}]
    }