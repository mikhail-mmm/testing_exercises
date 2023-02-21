import pytest

from functions.one_gender import genderalize


@pytest.mark.parametrize(
    'verb_male,verb_female,gender,expected',
    [
        ('verb_male', 'verb_female', 'male', 'verb_male'),
        ('verb_male', 'verb_female', 'female', 'verb_female'),
        ('verb_male', 'verb_female', 'test', 'verb_female'),
        ('verb_male', 'verb_female', 123, 'verb_female'),
        ('verb_male', 'verb_female', True, 'verb_female'),
        ('verb_male', 'verb_female', None, 'verb_female'),
        ('verb_male', 'verb_female', ['male', 'female'], 'verb_female'),
    ]
)
def test_genderalize(verb_male, verb_female, gender, expected):
    assert genderalize(verb_male, verb_female, gender) is expected
