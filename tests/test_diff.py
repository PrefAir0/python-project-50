from pathlib import Path

from gendiff import generate_diff


def get_fixture_path(filename):
    return Path('tests/test_data') / filename


def read_file(filename):
    return Path(filename).read_text()


def test_generate_diff():
    filepath1 = get_fixture_path('file1.json')
    filepath2 = get_fixture_path('file2.json')

    expected = read_file(get_fixture_path('expected.txt'))

    actual = generate_diff(filepath1, filepath2)

    assert actual == expected