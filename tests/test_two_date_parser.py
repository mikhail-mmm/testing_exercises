import datetime
import pytest

from conftest import datetime_today, datetime_tomorrow, time_str
from functions.two_date_parser import compose_datetime_from
from pytest_lazyfixture import lazy_fixture


@pytest.mark.parametrize(
    'date,time,expected',
    [
        ('tomorrow', lazy_fixture('time_str'), lazy_fixture('datetime_tomorrow')),
        ('today', lazy_fixture('time_str'), lazy_fixture('datetime_today')),
        ('21.02.20', lazy_fixture('time_str'), lazy_fixture('datetime_today')),
        (str(datetime.datetime.today), lazy_fixture('time_str'), lazy_fixture('datetime_today'))
    ]
)
def test_compose_datetime_from(date, time, expected):
    assert compose_datetime_from(date, time) == expected
