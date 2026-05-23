import pytest
from pathlib import Path
from gendiff import generate_diff


def get_fixture_path(filename):
    return Path('tests/test_data') / filename


def read_file(filename):
    return Path(filename).read_text()

@pytest.mark.parametrize("file1, file2, format_name, expected_file", [
    ('file1.json', 'file2.json', 'stylish', 'expected_stylish.txt'),
    ('file1.yaml', 'file2.yaml', 'stylish', 'expected_stylish.txt'),
    ('file1.json', 'file2.json', 'plain', 'expected_plain.txt'),
    ('file1.yaml', 'file2.yaml', 'plain', 'expected_plain.txt')
])
def test_generate_diff(file1, file2, format_name, expected_file):
    filepath1 = get_fixture_path(file1)
    filepath2 = get_fixture_path(file2)
    expected = read_file(get_fixture_path(expected_file))
    
    actual = generate_diff(filepath1, filepath2, format_name)
    
    assert actual == expected