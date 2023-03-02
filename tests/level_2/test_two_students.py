import pytest
from conftest import list_students_is_telegram_account, list_students_is_not_telegram_account, student
from pytest_lazyfixture import lazy_fixture
from functions.level_2.two_students import get_student_by_tg_nickname


@pytest.mark.parametrize(
    'telegram_username,students,expected',
    [
    ('test_account', lazy_fixture('list_students_is_telegram_account'), lazy_fixture('student')),
    ('test_account', lazy_fixture('list_students_is_not_telegram_account'), None),
    ]
)
def test_get_student_by_tg_nickname(telegram_username, students, expected):
    assert get_student_by_tg_nickname(telegram_username, students) == expected
