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
ra.remove("Banana")
print(ra)  # ['Apple', 'Cherry', 'Date', 'Elderberry', 'Orange', 'Blueberry', 'Peach', 'Pumpkin', 'Tomato']
ra.pop()
print(ra) # ['Apple', 'Cherry', 'Date', 'Elderberry', 'Orange', 'Blueberry', 'Peach', 'Pumpkin']
ra.pop()
print(ra) # ['Apple', 'Cherry', 'Date', 'Elderberry', 'Orange', 'Blueberry', 'Peach']
ra.pop()
print(ra) # ['Apple', 'Cherry', 'Date', 'Elderberry', 'Orange', 'Blueberry']
ra.pop()
print(ra) # ['Apple', 'Cherry', 'Date', 'Elderberry', 'Orange']
ra.insert(0, 'Popcorn')
print(ra) # ['Popcorn', 'Apple', 'Cherry', 'Date', 'Elderberry', 'Orange']
ra.insert(ra.size, 'Pizza')
print(ra) # ['Popcorn', 'Apple', 'Cherry', 'Date', 'Elderberry', 'Orange', 'Pizza']
ra.insert(3, 'Gatorage')
print(ra) # ['Popcorn', 'Apple', 'Cherry', 'Gatorage', 'Date', 'Elderberry', 'Orange', 'Pizza']
ra.removeAt(0)
print(ra) # ['Apple', 'Cherry', 'Gatorage', 'Date', 'Elderberry', 'Orange', 'Pizza']
ra.removeAt(3)
print(ra) # ['Apple', 'Cherry', 'Gatorage', 'Elderberry', 'Orange', 'Pizza']
ra.removeAt(ra.size - 1)
print(ra) # ['Apple', 'Cherry', 'Gatorage', 'Elderberry', 'Orange', 'Pizza']
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
- Iterator support and more built-in methods

## License

This project is open source and available under the MIT License.
