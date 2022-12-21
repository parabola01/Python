import pytest
from random_queue import RandomQueue

def test_queue():
    q = RandomQueue()
    inputs = [1, 2, 13, 'xyz']
    assert q.is_empty() == True

    q.insert(inputs[0])
    q.insert(inputs[1])
    q.insert(inputs[2])
    q.insert(inputs[3])

    assert q.is_full() == False
    assert q.is_empty() == False

    assert q.remove() in inputs

    with pytest.raises(ValueError):
        q.clear()
        q.remove()

