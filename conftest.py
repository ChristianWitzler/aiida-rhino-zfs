"""pytest fixtures for simplified testing."""
from __future__ import absolute_import
import pytest
pytest_plugins = ['aiida.manage.tests.pytest_fixtures']


@pytest.fixture(scope='function', autouse=True)
def clear_database_auto(clear_database):  # pylint: disable=unused-argument
    """Automatically clear database in between tests."""
    pass


@pytest.fixture(scope='function')
def rhino_zfs_code(aiida_local_code_factory):
    """Get a rhino_zfs code.
    """
    rhino_zfs_code = aiida_local_code_factory(executable='diff',
                                              entry_point='rhino_zfs')
    return rhino_zfs_code
