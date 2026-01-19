import pytest


def test_save_and_get_data(save_file, sample_data):
    save_file.save_data(sample_data[0])
    result = save_file.get_data("Python")
    assert len(result) == 1
    assert result[0]["name"] == "Python Developer"


def test_delete_data(save_file, sample_data):
    save_file.save_data(sample_data)
    save_file.del_data("Python Developer")
    result = save_file.get_data("Python")
    assert len(result) == 0
    result = save_file.get_data("Java")
    assert len(result) == 1


@pytest.mark.parametrize("keyword,expected_count", [
    ("Python", 1),
    ("Developer", 2),
    ("Manager", 0),
    ("python", 1),  # регистронезависимый
    ("DEVELOPER", 2),
])
def test_get_data_with_different_keywords(save_file, sample_data, keyword, expected_count):
    save_file.save_data(sample_data)
    result = save_file.get_data(keyword)
    assert len(result) == expected_count