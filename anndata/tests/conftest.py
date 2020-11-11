import pytest


@pytest.fixture
def backing_h5ad(tmp_path):
    return tmp_path / "test.h5ad"


def pytest_addoption(parser):
    parser.addoption('--useGpu', 
                     action='store', 
                     help='Run GPU Tests',
                     default=False,
                    )


@pytest.fixture
def use_gpu(request):
    return request.config.getoption("--useGpu") == 'True'