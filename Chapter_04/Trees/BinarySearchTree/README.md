# Binary Search Tree (BST) in Python

This project is a complete Binary Search Tree (BST) implementation in Python. It includes all core operations, visual printing, and both recursive and iterative versions of insert and search.

---

## Features

- Insert (Recursive & Iterative)
- Search (Recursive & Iterative)
- Delete Node (Handles 0, 1, 2 children)
- Inorder Traversal (Prints sorted keys)
- ASCII Tree Visualizer


---

## How to Use

```bash
python bst.py
```

You'll see:

- The sorted inorder traversal
- The visual structure of the tree
- Result of a search
- Tree after deletion of a node

---

## Core Concepts

### Node Structure

```python
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
```

Each node stores a value and two child pointers.

---

### Insert

#### Recursive
```python
def insert(self, key):
    def _insert(node, key):
        if node is None:
            return Node(key)
        ...
```

#### Iterative
```python
def insert_iterative(self, key):
    ...
```

---

### Search

```python
def search(self, key)
def search_iterative(self, key)
```

Returns the node if found, otherwise returns `None`.

---

### Delete

```python
def delete(self, key):
```

Handles:
- Node with no children (leaf)
- Node with one child
- Node with two children (uses in-order successor)

---

### Traversal

```python
def inorder_traversal(self):
```

Prints values in sorted order using in-order traversal.

---

### Visual Tree Print

```python
def print_tree(self):
```

Draws the tree using ASCII characters. For example:

```
|-- 15
|   |-- 12
10
|-- 5
    |-- 3
```

---

## Example Output

```
Inorder traversal (sorted):
3 5 7 10 12 15 18 

Visual Tree:
|-- 18
|   |-- 15
|       |-- 12
10
|   |-- 7
|-- 5
    |-- 3

Search 7: Found

Deleting 10 (root node)...
```

---

## Learning Goals

- Understand binary search tree structure and operations
- Learn recursive and iterative algorithm styles
- Visualize hierarchical data structures

---

## Author

Built by Paul Cloward

---

## License

MIT License