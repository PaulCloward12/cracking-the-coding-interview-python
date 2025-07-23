import pytest
from maxheap import MaxHeap

def test_insert_and_peek():
    heap = MaxHeap()
    heap.insert(10)
    heap.insert(5)
    heap.insert(30)
    heap.insert(20)
    assert heap.peek() == 30

def test_extract_max():
    heap = MaxHeap()
    for val in [15, 10, 25, 5, 40]:
        heap.insert(val)

    assert heap.extract_max() == 40
    assert heap.peek() == 25

def test_multiple_extractions():
    heap = MaxHeap()
    values = [50, 30, 20, 15, 10]
    for val in values:
        heap.insert(val)

    results = []
    while heap.peek() is not None:
        results.append(heap.extract_max())

    assert results == sorted(values, reverse=True)

def test_empty_extract():
    heap = MaxHeap()
    assert heap.extract_max() is None

def test_insert_single():
    heap = MaxHeap()
    heap.insert(99)
    assert heap.peek() == 99
    assert heap.extract_max() == 99
    assert heap.peek() is None