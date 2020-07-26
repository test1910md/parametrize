import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--logging",
        action="store",
        default="logging_file.txt",
        help="some logs",
    )


@pytest.fixture
def log_file(request):
    return request.config.getoption("--logging")
