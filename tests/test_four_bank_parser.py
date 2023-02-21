import datetime
import decimal
import pytest

from functions.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense
from pytest_lazyfixture import lazy_fixture


@pytest.fixture
def get_sms():
    return SmsMessage(
        text = '777 4545, 3333 10.03.20 10:35 10.02.20 authcode 324234234',
        author = 'Test_name',
        sent_at = datetime.datetime.today(),
    )


@pytest.fixture
def get_cards():
    return [
        BankCard(last_digits='3333', owner='First_test_name'),
        BankCard(last_digits='5555', owner='Second_test_name'),
    ]


@pytest.fixture
def get_expense(get_cards):
    return Expense(
        amount=decimal.Decimal('777'),
        card=get_cards[0],
        spent_in='10.02.20',
        spent_at=datetime.datetime(2020, 3, 10, 10, 35),
    )


@pytest.mark.parametrize(
    'sms,cards,expected',
    [
        (lazy_fixture('get_sms'), lazy_fixture('get_cards'), lazy_fixture('get_expense'))
    ]
)
def test_parse_ineco_expense(sms, cards, expected):
    assert parse_ineco_expense(sms, cards) == expected
