from functions.level_2.one_brackets import delete_remove_brackets_quotes
import pytest

@pytest.mark.parametrize(
    'name,name_without_brackets',
    [
        ('{{test_name}}', 'test_name'),
        ('test_name', 'test_name'),
        ('{test_name', 'est_na'),
    ]
)
def test_delete_remove_brackets_quotes(name, name_without_brackets):
    assert delete_remove_brackets_quotes(name) == name_without_brackets
