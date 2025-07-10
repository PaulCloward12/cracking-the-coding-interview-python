# 🧠 Hash Table with Chaining (Python)

This project demonstrates an educational yet powerful implementation of a Hash Table in Python using chaining with linked lists for collision resolution. It features an optimized polynomial rolling hash function, dynamic resizing based on load factor, and support for key operations like put(), get(), and remove(). The implementation helps reinforce key data structure concepts including hashing mechanics, collision handling, and scalable memory management.

---

## Features

- Stores key-value pairs
- Uses an optimized polynomial rolling hash function
- Handles collisions via chaining (lists of entries)
- Dynamically resizes the table when load factor exceeds 0.75
- Supports put(), get(), and remove() operations

---

## Getting Started

No external libraries required. Just run with Python 3.

```bash
python hashtable.py
```

---

## Example Usage

```python
for fruit in ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon"]:
    ht.put(fruit, len(fruit))

# Retrieve values
print(ht.get("apple"))   # Output: 5
print(ht.get("grape"))   # Output: 5
print(ht.get("lemon"))   # Output: 5

# Remove an entry
ht.remove("apple")
print(ht.get("apple"))   # Output: None

# Insert a duplicate key with a new value
ht.put("banana", 42)
print(ht.get("banana"))  # Output: 42

```
## To-Do

- Add support for key iteration
- Track and expose current load factor
- Implement optional shrinking to save memory
---

## How It Works

1. The hash_code() method converts a string key into a numeric hash using a polynomial rolling hash — multiplying by a prime number at each step to reduce collisions.
2. The hash value is then compressed into a valid array index using the modulo operator with the current table size.
3. Each index in the array holds a list of Entry objects, which store the actual key-value pairs.
4. When collisions occur, new entries are appended to the list at the same index.
5. If the load factor (# of entries / table size) exceeds 0.75, the table automatically resizes (doubles in size) and rehashes all entries.

---

## Example Output

```
5
5
5
None
42
---


## Learning Goals

- Understand how hash tables store and retrieve data efficiently
- Learn about collision resolution using chaining (linked lists)
- Implement an optimized hash function (polynomial rolling hash)
- Handle dynamic resizing based on load factor to maintain performance
- Practice designing scalable and modular data structures in Python
- Deepen understanding of hashing mechanics, including modulo-based indexing and entry rehashing during resize operations


---

## Author

Paul Cloward  
https://github.com/PaulCloward12  
Feel free to fork and modify!
