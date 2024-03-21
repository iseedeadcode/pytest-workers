import time
import pytest

@pytest.mark.parametrize("i", range(5))
def test_slow_operation(i):
    time.sleep(1)
    assert i >= 0

@pytest.mark.parametrize("i", range(3))
def test_quick_check(i):
    assert i in range(3)

@pytest.mark.parametrize("text", ["hello", "world", "pytest", "xdist"])
def test_string_operations(text):
    assert text.islower()
    assert len(text) > 0
