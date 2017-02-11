import pytest
import fibonacci

def test_naive():
    assert fibonacci.naive(0) == 0
    assert fibonacci.naive(1) == 1
    assert fibonacci.naive(2) == 1
    assert fibonacci.naive(3) == 2
    assert fibonacci.naive(4) == 3
    assert fibonacci.naive(5) == 5
    assert fibonacci.naive(25) == 75025
# too slow
#    assert fibonacci.naive(40) == 102334155

def test_memoized():
    assert fibonacci.memoized(0) == 0
    assert fibonacci.memoized(1) == 1
    assert fibonacci.memoized(2) == 1
    assert fibonacci.memoized(3) == 2
    assert fibonacci.memoized(4) == 3
    assert fibonacci.memoized(5) == 5
    assert fibonacci.memoized(25) == 75025
    assert fibonacci.memoized(40) == 102334155

def test_tabulation():
    assert fibonacci.tabulation(0) == 0
    assert fibonacci.tabulation(1) == 1
    assert fibonacci.tabulation(2) == 1
    assert fibonacci.tabulation(3) == 2
    assert fibonacci.tabulation(4) == 3
    assert fibonacci.tabulation(5) == 5
    assert fibonacci.tabulation(25) == 75025
    assert fibonacci.tabulation(40) == 102334155

if __name__ == '__main__':
    pytest.main()
