import pytest

from functions.three_url_builder import build_url


@pytest.mark.parametrize(
    'host_name,relative_url,get_params,expected',
    [
        ('host_name', 'test_url', {'a': 'test_a', 'b': 'test_b'}, 'host_name/test_url?a=test_a&b=test_b'),
        ('host_name', 'test_url', {'a': 'test_a'}, 'host_name/test_url?a=test_a'),
        ('host_name', 'test_url', {}, 'host_name/test_url'),
        ('host_name', 'test_url', None, 'host_name/test_url'),
    ]
)
def test_build_url(host_name, relative_url, get_params, expected):
    assert build_url(host_name, relative_url, get_params) == expected
