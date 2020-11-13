import pytest


@pytest.fixture
def backing_h5ad(tmp_path):
    return tmp_path / "test.h5ad"


def pytest_addoption(parser):
    parser.addoption('--hw', 
                     action='store', 
                     help='HW type',
                     default='cpu',
                    )


def pytest_configure(config):
    config.addinivalue_line(
        "markers", 
        "skipif_hw(hw): Skip this test for the given hardware")


def pytest_runtest_setup(item):
    hw_type = [mark.args[0] for mark in item.iter_markers(name="skipif_hw")]
    if hw_type:
        if item.config.getoption("--hw") in hw_type:
            pytest.skip("Test skipped for {!r}".format(hw_type))


@pytest.fixture
def use_gpu(request):
    use_gpu = request.config.getoption("--hw") == 'gpu'
    request.config.use_gpu = use_gpu
    return use_gpu