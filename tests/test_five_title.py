import pytest

from conftest import long_title
from functions.five_title import change_copy_item
from pytest_lazyfixture import lazy_fixture


@pytest.mark.parametrize(
    'title,expected',
    [
        (lazy_fixture('long_title'), lazy_fixture('long_title')),
        ("A-ha: Take on me", "Copy of A-ha: Take on me"),
        ("Copy of A-ha: Take on me", "Copy of A-ha: Take on me (2)"),
        ("Copy of A-ha: Take on me (2)", "Copy of A-ha: Take on me (3)"),
    ]
)
def test_change_copy_item(title, expected):
    assert change_copy_item(title) == expected
