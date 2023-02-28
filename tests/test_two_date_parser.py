from datetime import datetime
import pytest

from functions.two_date_parser import compose_datetime_from


@pytest.mark.parametrize(
    'date,time,expected',
    [
        ('tomorrow', '10:30', datetime(2023, 3, 1, 10, 30)),
        ('today', '10:30', datetime(2023, 2, 28, 10, 30)),
        ('21.02.20', '10:30', datetime(2023, 2, 28, 10, 30)),
    ]
)
def test_compose_datetime_from(date, time, expected):
    assert compose_datetime_from(date, time) == expected
