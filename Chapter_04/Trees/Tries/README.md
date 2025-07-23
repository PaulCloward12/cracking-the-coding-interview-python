# Trie (Prefix Tree) in Python

## Overview

A **Trie** (pronounced "try") is a tree-like data structure used for storing strings. It's especially useful for tasks involving prefix lookups, such as autocomplete or dictionary-based searches.

## Structure

Each node in the Trie has:

- A dictionary of child nodes (`children`)
- A boolean flag indicating whether the current node represents the end of a word (`is_end_of_word`)

## Supported Operations

- `insert(word)`: Add a word to the Trie
- `search(word)`: Return True if the full word exists in the Trie
- `starts_with(prefix)`: Return True if any word in the Trie starts with the given prefix

## Example Usage

```python
trie = Trie()
trie.insert("apple")
trie.search("apple")     # True
trie.search("app")       # False
trie.starts_with("app")  # True
trie.insert("app")
trie.search("app")       # True

## Example Usage 2

trie = Trie()
words = ["apple", "app", "bat", "ball", "bark"]
for word in words:
    trie.insert(word)

trie.visualize()
