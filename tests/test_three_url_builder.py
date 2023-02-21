import pytest

from functions.three_url_builder import build_url
from pytest_lazyfixture import lazy_fixture


@pytest.fixture
def get_dict():
    return {
        'a': 'test_a',
        'b': 'test_b'
    }

@pytest.fixture
def get_querypart(get_dict):
    return '?' + '&'.join([f'{k}={v}' for (k, v) in get_dict.items()])


@pytest.fixture
def get_host_name():
    return 'host_name'


@pytest.fixture
def get_relative_url():
    return 'test_url'


@pytest.fixture
def get_url_with_params(get_host_name, get_relative_url, get_querypart):
    return f'{get_host_name}/{get_relative_url}{get_querypart}'


@pytest.fixture
def get_url_without_params(get_host_name, get_relative_url):
    return f'{get_host_name}/{get_relative_url}'


@pytest.mark.parametrize(
    'host_name,relative_url,get_params,expected',
    [
        (lazy_fixture('get_host_name'), lazy_fixture('get_relative_url'), lazy_fixture('get_dict'), lazy_fixture('get_url_with_params')),
        (lazy_fixture('get_host_name'), lazy_fixture('get_relative_url'), None, lazy_fixture('get_url_without_params')),
    ]
)
def test_build_url(host_name, relative_url, get_params, expected):
    assert build_url(host_name, relative_url, get_params) == expected
