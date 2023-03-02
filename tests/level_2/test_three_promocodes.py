from functions.level_2.three_promocodes import generate_promocode


def test__generate_promocode__capital_letters(len_string=8):
    result = generate_promocode(len_string)
    assert result == result.upper()


def test__generate_promocode__len_string(len_string=8):
    assert len(generate_promocode(len_string)) == len_string


def test__generate_promocode__letters_only(len_string=8):
    assert (generate_promocode(len_string)).isalpha() == True
