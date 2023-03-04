import pytest
from conftest import students_with_telegram_account, students_without_telegram_account, student
from pytest_lazyfixture import lazy_fixture
from functions.level_2.two_students import get_student_by_tg_nickname


@pytest.mark.parametrize(
    'telegram_username,students,expected',
    [
        ('test_account', lazy_fixture('students_with_telegram_account'), lazy_fixture('student')),
        ('test_account', lazy_fixture('students_without_telegram_account'), None),
    ]
)
def test_get_student_by_tg_nickname(telegram_username, students, expected):
    assert get_student_by_tg_nickname(telegram_username, students) == expected
