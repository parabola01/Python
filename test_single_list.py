import pytest
from single_list import SingleList, Node

def test_min():
    n1 = Node(2)
    n2 = Node(10)
    n3 = Node(13)
    n4 = Node(1)
    n5 = Node(5)
    lt = SingleList()
    lt.insert_head(n1)
    lt.insert_head(n2)
    lt.insert_head(n3)
    lt.insert_head(n4)
    lt.insert_head(n5)

    assert lt.find_min() == n4

def test_max():
    n1 = Node(2)
    n2 = Node(10)
    n3 = Node(13)
    n4 = Node(1)
    n5 = Node(5)
    lt = SingleList()
    lt.insert_head(n1)
    lt.insert_head(n2)
    lt.insert_head(n3)
    lt.insert_head(n4)
    lt.insert_head(n5)

    assert lt.find_max() == n3

def test_search_():
    n1 = Node(2)
    n2 = Node(10)
    n3 = Node(13)
    n4 = Node(1)
    n5 = Node(5)
    lt = SingleList()
    lt.insert_head(n1)
    lt.insert_head(n2)
    lt.insert_head(n3)
    lt.insert_head(n4)
    lt.insert_head(n5)

    assert lt.search(2) == n1
    assert lt.search(1) == n4
    assert lt.search(5) == n5


def test_reverse():
        n1 = Node(2)
        n2 = Node(10)
        n3 = Node(13)
        n4 = Node(1)
        n5 = Node(5)
        lt = SingleList()
        lt.insert_head(n1)
        lt.insert_head(n2)
        lt.insert_head(n3)
        lt.insert_head(n4)
        lt.insert_head(n5)

        lt1 = []
        for item in lt:
            lt1.append(lt)

        lt2 = SingleList()
        lt2.insert_head(n1)
        lt2.insert_head(n2)
        lt2.insert_head(n3)
        lt2.insert_head(n4)
        lt2.insert_head(n5)

        lt3 = []
        for item in lt2:
            lt3.append(lt)

        assert lt1 == lt3




