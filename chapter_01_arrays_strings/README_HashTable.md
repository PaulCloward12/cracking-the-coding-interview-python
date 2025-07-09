# 🧠 Hash Table with Chaining (Python)

This project demonstrates a simple implementation of a **Hash Table using chaining with linked lists** in Python. It's designed for educational purposes and helps illustrate how hash codes, modulo-based indexing, and collision resolution work.

---

## 📦 Features

- Stores key-value pairs
- Uses a simple hash function
- Handles collisions via chaining (lists of entries)
- Supports `put()` and `get()` operations

---

## 🚀 Getting Started

No external libraries required. Just run with Python 3.

```bash
python3 hashtable.py
```

---

## 🧩 Example Usage

```python
ht = HashTable()
ht.put("apple", 100)
ht.put("grape", 250)
ht.put("cat", 200)

print(ht.get("apple"))  # Output: 100
print(ht.get("grape"))  # Output: 250
print(ht.get("cat"))    # Output: 200
```

---

## 🔍 How It Works

1. The `hash_code()` method converts a string key into an integer by summing the Unicode values of its characters.
2. The hash value is compressed into a valid array index using the modulo operator.
3. Each index in the array holds a **list of `Entry` objects**, which stores key-value pairs.
4. When collisions occur, entries are appended to the list at the same index.

---

## 🧪 Example Output

```
100
250
200
```

---

## 📂 File Structure

```
hashtable.py       # Core implementation
README.md          # Documentation
```

---

## 📘 Learning Goals

- Understand the mechanics behind hash tables
- Learn basic collision handling using chaining
- Practice object-oriented Python design

---

## 🛠️ To-Do

- Add delete functionality
- Optimize hash function
- Dynamically resize the table when load factor increases

---

## 🧑‍💻 Author

Paul Cloward  
[GitHub Profile (Optional)](https://github.com/your-username)  
Feel free to fork and modify!
