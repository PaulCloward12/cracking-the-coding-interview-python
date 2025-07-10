# ArrayList and Resizable Arrays (Python)

# ResizableArray in Python

This project demonstrates a simple implementation of a **resizable array** in Python, similar in behavior to Java's `ArrayList`.

## Features

- Dynamic resizing when capacity is exceeded
- Constant-time (amortized) insertion at the end
- Direct access by index
- Clear, beginner-friendly implementation

## 🔍 How It Works

1. The array starts with an initial capacity (default: 4).
2. When the array is full, it **doubles in size**.
3. Elements are copied to the new, larger array during resizing.
4. New values can be added using the `add()` method.
5. Values can be accessed using the `get()` method.

## Example Usage

```python
ra = ResizableArray()
ra.add("Apple")
ra.add("Banana")
ra.add("Cherry")
ra.add("Date")
ra.add("Elderberry")
print(ra)  # Output: ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
ra.add("Orange")
ra.add("Blueberry")
ra.add("Peach")
ra.add("Pumpkin")
ra.add("Tomato")
print(ra)  # ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Orange', 'Blueberry', 'Peach', 'Pumpkin', 'Tomato']
```

## Time Complexities

| Operation          | Time Complexity |
|--------------------|-----------------|
| Add (end)          | O(1) amortized  |
| Access by index    | O(1)            |
| Resize (when full) | O(n)            |

## File Structure

- `ResizableArray_Python.py` - Main Python code
- `README.md` - Project documentation

## Future Enhancements

- Implement `remove()` method
- Support for insertion/removal at arbitrary indices
- Iterator support and more built-in methods

## License

This project is open source and available under the MIT License.
