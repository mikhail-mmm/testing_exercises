import datetime
import pytest

from functions.two_date_parser import compose_datetime_from
from pytest_lazyfixture import lazy_fixture


@pytest.fixture
def minute():
    return 25


@pytest.fixture
def hour():
    return 10


@pytest.fixture
def get_time_str(hour, minute):
    return f'{str(hour)}:{str(minute)}'


@pytest.fixture
def expected_today(hour, minute):
    date = datetime.datetime.today()
    return datetime.datetime(
        date.year,
        date.month,
        date.day,
        hour,
        minute,
    )


@pytest.fixture
def expected_tomorrow(hour, minute):
    date = datetime.datetime.today() + datetime.timedelta(days=1)
    return datetime.datetime(
        date.year,
        date.month,
        date.day,
        hour,
        minute,
    )


@pytest.mark.parametrize(
    'date_str,time_str,expected',
    [
        ('tomorrow', lazy_fixture('get_time_str'), lazy_fixture('expected_tomorrow')),
        ('today', lazy_fixture('get_time_str'), lazy_fixture('expected_today')),
        ('21.02.20', lazy_fixture('get_time_str'), lazy_fixture('expected_today')),
        (str(datetime.datetime.today), lazy_fixture('get_time_str'), lazy_fixture('expected_today'))
    ]
)
def test_compose_datetime_from(date_str, time_str, expected):
    assert compose_datetime_from(date_str, time_str) == expected
