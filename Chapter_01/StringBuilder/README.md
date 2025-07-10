# Efficient String Manipulation in Python

This project demonstrates how to perform efficient string operations in Python by **emulating the Java `StringBuilder` pattern**. Since Python strings are immutable, naive concatenation can lead to performance issues. This guide shows the right way to build and manipulate strings efficiently.

---

## Why Not Use `+=` in a Loop?

In Python, this:

```python
s = ""
for i in range(100):
    s += str(i)
```

Creates a **new string on every iteration** because strings are immutable.  
 **Time Complexity: O(n²)**

---

## Use a List and `join()` Instead

```python
parts = []
for i in range(100):
    parts.append(str(i))
s = ''.join(parts)
```

**Time Complexity: O(n)**  
Much more efficient — appending to a list is fast, and `''.join()` is optimized.

---

## Example Functions

### Reverse a String (Efficiently)

```python
def reverse_string(s):
    chars = list(s)
    chars.reverse()
    return ''.join(chars)

# Output: "weivretni"
print(reverse_string("interview"))
```

### Reverse a String (Using Loop)

```python
def reverse_string_loop(s):
    result = []
    for i in range(len(s) - 1, -1, -1):
        result.append(s[i])
    return ''.join(result)
```

---

## Interview Tip

In coding interviews, whenever you're building or modifying a string many times (especially in loops or recursive solutions), use this **"StringBuilder" pattern in Python**:

- Create a `list` of string fragments
- Use `''.join(list)` at the end to convert to a final string

This approach keeps your solution **fast and memory-efficient**.

---

## Further Reading

- [Python Docs: str.join()](https://docs.python.org/3/library/stdtypes.html#str.join)
- [Java Docs: StringBuilder](https://docs.oracle.com/javase/8/docs/api/java/lang/StringBuilder.html)
