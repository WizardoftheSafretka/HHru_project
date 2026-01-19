import os
import tempfile

import pytest

from src.save_file import SaveFile


@pytest.fixture()
def test_vacancy():
    return {
        "items": [{"name": "Developer"}, {"name": "Manager"}]
    }


@pytest.fixture()
def save_file(self):
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_file_name = f.name
    save_file = SaveFile(temp_file_name)
    yield save_file
    if os.path.exists(temp_file_name):
        os.unlink(temp_file_name)

@pytest.fixture()
def sample_data(self):
    return [
        {
            "name": "Python Developer",
            "responsibility": "Разработка на Python",
            "salary": 100000
        },
        {
            "name": "Java Developer",
            "responsibility": "Разработка на Java",
            "salary": 120000
        }
    ]