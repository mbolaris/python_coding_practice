import pytest
import q_1_1

def test_is_unique():
    assert q_1_1.is_unique("abcd") == True
    assert q_1_1.is_unique("abca") == False
if __name__ == '__main__':
    pytest.main()