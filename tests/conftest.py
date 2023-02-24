import datetime
import decimal
import pytest

from functions.four_bank_parser import BankCard, SmsMessage, Expense


@pytest.fixture
def expected_today():
    date = datetime.datetime.today()
    return datetime.datetime(
        date.year,
        date.month,
        date.day,
        10,
        25,
    )


@pytest.fixture
def expected_tomorrow():
    date = datetime.datetime.today() + datetime.timedelta(days=1)
    return datetime.datetime(
        date.year,
        date.month,
        date.day,
        10,
        25,
    )


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
    return """We're talking away I don't know what I'm to say I'll say it anyway 
Today's another day to find you Shying away I'll be coming for your love, okay? 
Take on me (Take on me) Take me on (Take on me) I'll be gone In a day or two 
So needless to say I'm odds and ends But I'll be stumbling away 
Slowly learning that life is okay Say after me 
It's no better to be safe than sorry 
Take on me (Take on me) Take me on (Take on me) 
I'll be gone In a day or two Oh, things that you say 
Is it a life or just to play my worries away? You're all the things 
I've got to remember You're shying away I'll be coming for you anyway 
Take on me (Take on me) Take me on (Take on me) I'll be gone In a day 
Take on me (Take on me) Take me on (Take on me) I'll be gone In a day
"""
