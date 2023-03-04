import pytest

from functions.level_2.five_extra_fields import fetch_extra_fields_configuration, fetch_app_config_field


@pytest.mark.parametrize(
    'filename,expected',
    [
        ('test_config_with_all.conf', {'test': str}),
        ('test_config_without_extra_fields.conf', {}),
    ]
)
def test_fetch_extra_fields_configuration(filename, expected):
    config_file_path = f'tests/level_2/test_files/{filename}'
    assert fetch_extra_fields_configuration(config_file_path) == expected


@pytest.mark.parametrize(
    'filename,expected',
    [
        ('test_config_with_all.conf', '\ntest: str'),
        ('test_config_without_app_cofig.conf', None),
    ]
)
def test_fetch_app_config_field(filename, expected):
    config_file_path = f'tests/level_2/test_files/{filename}'
    assert fetch_app_config_field(config_file_path, 'extra_fields') == expected
