import pytest
from functions.level_2.two_students import Student


@pytest.fixture
def list_students_is_telegram_account():
    students = []
    students.append(
        Student(
        first_name='test_name',
        last_name='test_last_name',
        telegram_account='@test_account',
        ))
    students.append(
        Student(
        first_name='test_name_2',
        last_name='test_last_name_2',
        telegram_account='test_account',
        ))
    return students


@pytest.fixture
def student(list_students_is_telegram_account):
    return list_students_is_telegram_account[0]


@pytest.fixture
def list_students_is_not_telegram_account():
    students = []
    students.append(
        Student(
        first_name='test_name',
        last_name='test_last_name',
        telegram_account=None,
        ))
    students.append(
        Student(
        first_name='test_name_2',
        last_name='test_last_name_2',
        telegram_account=None,
        ))
    return students
