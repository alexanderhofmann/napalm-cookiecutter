"""Test fixtures."""
from builtins import super

import pytest
from napalm_base.test import conftest as parent_conftest

from napalm_base.test.double import BaseTestDouble

from {{cookiecutter.module_name}} import {{cookiecutter.driver_name}}


@pytest.fixture(scope='class')
def set_device_parameters(request):
    """Set up the class."""
    def fin():
        request.cls.device.close()
    request.addfinalizer(fin)

    request.cls.driver = {{cookiecutter.driver_name}}.{{cookiecutter.capitalized_name}}Driver
    request.cls.patched_driver = Patched{{cookiecutter.capitalized_name}}Driver
    request.cls.vendor = '{{cookiecutter.driver_name}}'
    parent_conftest.set_device_parameters(request)


def pytest_generate_tests(metafunc):
    """Generate test cases dynamically."""
    parent_conftest.pytest_generate_tests(metafunc, __file__)


class Patched{{cookiecutter.capitalized_name}}Driver({{cookiecutter.driver_name}}.{{cookiecutter.capitalized_name}}Driver):
    """Patched {{cookiecutter.capitalized_name}} Driver."""

    def __init__(self, hostname, username, password, timeout=60, optional_args=None):
        super().__init__(hostname, username, password, timeout, optional_args)

        self.patched_attrs = ['device']
        self.device = Fake{{cookiecutter.capitalized_name}}Device()


class Fake{{cookiecutter.capitalized_name}}Device(BaseTestDouble):
    """{{cookiecutter.capitalized_name}} device test double."""

    def run_commands(self, command_list, encoding='json'):
        """Fake run_commands."""
        result = list()

        for command in command_list:
            filename = '{}.{}'.format(self.sanitize_text(command), encoding)
            full_path = self.find_file(filename)

            if encoding == 'json':
                result.append(self.read_json_file(full_path))
            else:
                result.append({'output': self.read_txt_file(full_path)})

        return result
