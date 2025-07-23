
# Binary Min Heap in Python

This project demonstrates how to build a **Binary Min Heap** from scratch using Python. A Min Heap is a complete binary tree where the parent node is always less than or equal to its children.

## Features

- Insert elements into the heap
- Extract the minimum element
- Peek at the minimum element
- Maintains the heap property automatically

## How It Works

### Insertion (`insert`)
- New element is added to the end of the list.
- It is then moved up ("heapify up") until the heap property is restored.

### Extract Minimum (`extract_min`)
- The root (minimum element) is removed.
- The last element is moved to the root and moved down ("heapify down") to maintain the heap.

## Example

```python
h = MinHeap()
h.insert(10)
h.insert(4)
h.insert(15)
h.insert(1)
print(h)          # Output: [1, 4, 15, 10]
print(h.extract_min())  # Output: 1
print(h)          # Output: [4, 10, 15]
```

## Files

- `min_heap.py`: The main class implementation
- `README.md`: This guide

## Perfect for Beginners

No external libraries required. This is pure Python code written for educational purposes!

