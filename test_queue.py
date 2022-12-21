import pytest
from queue import Queue

def test_queue():
    q = Queue()
    assert q.is_empty() == True

    q.put(1)
    q.put(2)
    q.put(13)
    q.put("xyz")

    assert q.is_full() == False
    assert q.is_empty() == False

    assert q.get() == 1
    assert q.get() == 2
    assert q.get() == 13
    assert q.get() == 'xyz'


    with pytest.raises(ValueError):
        q.get()







