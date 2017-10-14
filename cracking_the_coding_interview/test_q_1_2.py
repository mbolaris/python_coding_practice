import pytest
import q_1_2

def test_is_unique():
    assert q_1_2.is_permutation("abcd", "dbca") == True
    assert q_1_2.is_permutation("abca", "aaaa") == False
    assert q_1_2.is_permutation("KaiBolarisIsAwesome!",
                                "xxxxxxxxxxxxxxxxxxxx") == False
    assert q_1_2.is_permutation("", "xxxxxxxxxxxxxxxxxxxx") == False
    assert q_1_2.is_permutation("", "") == True
if __name__ == '__main__':
    pytest.main()