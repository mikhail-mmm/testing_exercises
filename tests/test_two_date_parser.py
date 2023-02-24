import datetime
import pytest

from conftest import expected_today, expected_tomorrow
from functions.two_date_parser import compose_datetime_from
from pytest_lazyfixture import lazy_fixture


@pytest.mark.parametrize(
    'date,time,expected',
    [
        ('tomorrow', '10:25', lazy_fixture('expected_tomorrow')),
        ('today', '10:25', lazy_fixture('expected_today')),
        ('21.02.20', '10:25', lazy_fixture('expected_today')),
        (str(datetime.datetime.today), '10:25', lazy_fixture('expected_today'))
    ]
)
def test_compose_datetime_from(date, time, expected):
    assert compose_datetime_from(date, time) == expected
