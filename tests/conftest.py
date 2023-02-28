import datetime
import decimal
import pytest

from faker import Faker
from functions.four_bank_parser import BankCard, SmsMessage, Expense


@pytest.fixture
def sms():
    return SmsMessage(
        text='777 4545, 3333 10.03.20 10:35 10.02.20 authcode 324234234',
        author='Test_name',
        sent_at=datetime.datetime.today(),
    )


@pytest.fixture
def cards():
    return [
        BankCard(last_digits='3333', owner='First_test_name'),
        BankCard(last_digits='5555', owner='Second_test_name'),
    ]


@pytest.fixture
def expense(cards):
    return Expense(
        amount=decimal.Decimal('777'),
        card=cards[0],
        spent_in='10.02.20',
        spent_at=datetime.datetime(2020, 3, 10, 10, 35),
    )


@pytest.fixture
def long_title():
    fake = Faker(locale="en_US")
    fake_long_title = ''
    for _ in range(0, 2):
        fake_long_title += fake.text()
    return fake_long_title
