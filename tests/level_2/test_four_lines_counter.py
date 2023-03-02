import pytest

from functions.level_2.four_lines_counter import count_lines_in


@pytest.mark.parametrize(
    'filepath,expected',
    [
    ('tests/level_2/test_files/test_file_with_four_lines.txt', 4),
    ('tests/level_2/test_files/test_file_with_one_line.txt', 1),
    ('tests/level_2/test_files/test_file_without_lines.txt', 0),
    ('tests/level_2/test_files/non_exist_file.txt', None),
    ]
)
def test_count_lines_in(filepath, expected):
    assert count_lines_in(filepath) == expected
