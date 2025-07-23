# Binary Max-Heap (Node-Based) in Python

This project demonstrates a binary max-heap implementation using a node-based structure in Python. A max-heap is a complete binary tree where the value of each node is greater than or equal to the values of its children.

## Features

- `insert(key)`: Adds a new element to the heap while maintaining the max-heap property.
- `extract_max()`: Removes and returns the largest element (root) from the heap.
- `peek()`: Returns the maximum value without removing it.
- `print_heap()`: Prints the current heap in level order.

## Structure

Internally, we use a list (`self.nodes`) to simulate the level-order structure of a complete binary tree. Each element is a `Node` object, and their left and right references are maintained manually to simulate a tree.

## Example

```python
heap = MaxHeap()
heap.insert(10)
heap.insert(20)
heap.insert(5)
heap.insert(30)

heap.print_heap()       # Output: [30, 20, 5, 10]
print(heap.peek())      # Output: 30
print(heap.extract_max()) # Output: 30
heap.print_heap()       # Output: [20, 10, 5]
```

## How to Test 
pytest test_maxheap.py  