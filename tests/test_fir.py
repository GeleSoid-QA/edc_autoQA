import pytest

@pytest.fixture()
def before_after():
    print("before")
    yield
    print ("\nAfter")



def test_demo1():
    assert 1 == 1

def test_demo2(before_after):
    a=5
    b=5
    assert a == b
