import pytest
from functions.level_2.two_students import Student


@pytest.fixture
def students_with_telegram_account():
    students = []
    students.append(
        Student(
            first_name='test_name',
            last_name='test_last_name',
            telegram_account='@test_account',
        )
    )
    students.append(
        Student(
            first_name='test_name_2',
            last_name='test_last_name_2',
            telegram_account='@test_account_2',
        )
    )
    return students


@pytest.fixture
def student(students_with_telegram_account):
    return students_with_telegram_account[0]


@pytest.fixture
def students_without_telegram_account(students_with_telegram_account):
    students = []
    students.append(
        Student(
            first_name='test_name',
            last_name='test_last_name',
            telegram_account=None,
        )
    )
    students.append(
        Student(
            first_name='test_name_2',
            last_name='test_last_name_2',
            telegram_account=None,
        )
    )
    return students
