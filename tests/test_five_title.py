import pytest

from conftest import long_title
from functions.five_title import change_copy_item
from pytest_lazyfixture import lazy_fixture


@pytest.mark.parametrize(
    'title,expected',
    [
        (lazy_fixture('long_title'), lazy_fixture('long_title')),
        ("Test", "Copy of Test"),
        ("Copy of Test", "Copy of Test (2)"),
        ("Copy of Test (2)", "Copy of Test (3)"),
    ]
)
def test_change_copy_item(title, expected):
    assert change_copy_item(title) == expected
