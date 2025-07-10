# ResizableArray in Python

This project demonstrates a simple implementation of a **resizable array** in Python, similar in behavior to Java's `ArrayList`.

## Features

- Dynamic resizing when capacity is exceeded
- Constant-time (amortized) insertion at the end
- Direct access by index
- Remove elements by value or by index
- Insert elements at any index
- Pop elements from the end (stack-like behavior)
- Clear, beginner-friendly implementation

## How It Works

1. The array starts with an initial capacity (default: 4).
2. When the array is full, it **doubles in size**.
3. Elements are copied to the new, larger array during resizing.
4. New values can be added using the `add()` method.
5. Values can be accessed using the `get()` method.
6. The `remove()` method deletes the first occurrence of a value.
7. The `remove_at(index)` method removes a value at a specific index.
8. The `insert(index, value)` method inserts a value at a specific index by shifting elements right.
9. The `pop()` method removes and returns the last element.

## Example Usage

```python
ra = ResizableArray()
ra.add("A")
ra.add("B")
ra.add("C")
ra.insert(1, "X")      # ['A', 'X', 'B', 'C']
ra.remove_at(2)        # ['A', 'X', 'C']
print(ra)

last = ra.pop()        # Removes 'C'
print(last)            # Output: 'C'
print(ra)              # Output: ['A', 'X']
```

## Time Complexities

| Operation           | Time Complexity |
|---------------------|-----------------|
| Add at end          | O(1) amortized  |
| Access by index     | O(1)            |
| Remove at end (pop) | O(1)            |
| Insert in middle    | O(n)            |
| Remove in middle    | O(n)            |

## File Structure

- `ResizableArray_Python.py` - Main Python code
- `README.md` - Project documentation

## Future Enhancements

- Iterator support for loops (e.g. `for item in ra`)
- Shrinking array when many elements are removed
- `contains()` and `index_of()` utility methods

## License

This project is open source and available under the MIT License.
