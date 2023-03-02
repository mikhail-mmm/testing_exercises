import pytest

from functions.level_2.five_extra_fields import fetch_extra_fields_configuration, fetch_app_config_field


@pytest.mark.parametrize(
    'config_file_path,expected',
    [
    ('tests/level_2/test_files/test_config_with_all.conf', {'test': str}),
    ('tests/level_2/test_files/test_config_without_extra_fields.conf', {}),
    ]
)
def test_fetch_extra_fields_configuration(config_file_path, expected):
    assert fetch_extra_fields_configuration(config_file_path) == expected


@pytest.mark.parametrize(
    'config_file_path,expected',
    [
    ('tests/level_2/test_files/test_config_with_all.conf', '\ntest: str'),
    ('tests/level_2/test_files/test_config_without_app_cofig.conf', None),
    ]
)
def test_fetch_app_config_field(config_file_path, expected):
    assert fetch_app_config_field(config_file_path, 'extra_fields') == expected
