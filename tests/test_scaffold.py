import subprocess
import tomllib
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope='module')
def pyproject() -> dict:
    with (ROOT / 'pyproject.toml').open('rb') as handle:
        return tomllib.load(handle)


def test_should_import_package_when_installed() -> None:
    import src

    assert src is not None


def test_should_name_project_when_pyproject_read(pyproject: dict) -> None:
    assert pyproject['project']['name'] == 'ml-prediction-api'


def test_should_require_python_312_when_pyproject_read(pyproject: dict) -> None:
    assert pyproject['project']['requires-python'] == '>=3.12'


def test_should_provide_env_example_when_repository_checked() -> None:
    assert (ROOT / '.env.example').is_file()


def test_should_not_track_env_file_when_repository_checked() -> None:
    tracked = subprocess.run(
        ['git', 'ls-files', '.env'],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )

    assert tracked.stdout.strip() == ''


def test_should_provide_rules_when_repository_checked() -> None:
    assert list((ROOT / 'rules').glob('*.md'))


def test_should_provide_sync_script_when_repository_checked() -> None:
    assert (ROOT / 'scripts' / 'sync-rules.sh').is_file()
