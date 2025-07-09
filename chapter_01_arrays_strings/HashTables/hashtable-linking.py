class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self, size=5):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash_code(self, key):
        return sum(ord(c) for c in key)

    def put(self, key, value):
        index = self.hash_code(key) % self.size
        bucket = self.buckets[index]
        for entry in bucket:
            if entry.key == key:
                entry.value = value  # Update
                return
        bucket.append(Entry(key, value))  # Insert

    def get(self, key):
        index = self.hash_code(key) % self.size
        bucket = self.buckets[index]
        for entry in bucket:
            if entry.key == key:
                return entry.value
        return None

# Demo
ht = HashTable()
ht.put("apple", 100)
ht.put("grape", 250)
ht.put("cat", 200)

print(ht.get("apple"))  # 100
print(ht.get("grape"))  # 250
print(ht.get("cat"))    # 200
