import pytest

from fixture.controller import Controller


@pytest.fixture(scope='session')
def app(request):
    url = request.config.getoption('--api-url')
    return Controller(url)


def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action='store',
        help='input url api',
        default="https://stores-tests-api.herokuapp.com",
    ),
