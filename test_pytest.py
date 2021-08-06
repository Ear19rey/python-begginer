from hypothesis import given
import hypothesis.strategies as some

@given(some.lists(some.integers(min_value=1),max_size=100))
def test_abc(a_list):
    ol = len(a_list)
    a_list.sort()
    assert len(a_list) == ol

@given(some.lists(some.text()))
def test_dsa(a_list):
    a_list.sort()
    for i in range(len(a_list)-1):
        assert a_list[i] <= a_list[i+1]
