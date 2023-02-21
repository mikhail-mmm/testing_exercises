import pytest

from functions.five_title import change_copy_item
from pytest_lazyfixture import lazy_fixture
from titles import TITLE1, TITLE2


@pytest.fixture
def create_title_with_additional_copy_text():
    return f'Copy of {TITLE2}'


@pytest.fixture
def creating_duplicate_title(create_title_with_additional_copy_text):
    return f'{create_title_with_additional_copy_text} (2)'


@pytest.fixture
def creating_next_duplicate_title(create_title_with_additional_copy_text):
    return f'{create_title_with_additional_copy_text} (3)'


@pytest.mark.parametrize(
    'title,expected',
    [
        (TITLE1, TITLE1),
        (TITLE2, lazy_fixture('create_title_with_additional_copy_text')),
        (lazy_fixture('create_title_with_additional_copy_text'), lazy_fixture('creating_duplicate_title')),
        (lazy_fixture('creating_duplicate_title'), lazy_fixture('creating_next_duplicate_title')),
    ]
)
def test_change_copy_item(title, expected):
    assert change_copy_item(title) == expected
