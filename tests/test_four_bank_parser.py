from conftest import sms, cards, expense
from functions.four_bank_parser import parse_ineco_expense


def test_parse_ineco_expense(sms, cards, expense):
    assert parse_ineco_expense(sms, cards) == expense
