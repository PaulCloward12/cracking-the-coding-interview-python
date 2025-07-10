class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self, size=5):
        self.size = size
        self.buckets = [[] for _ in range(size)]  # Array of lists

    def hash_code(self, key):
        # Optimized polynomial rolling hash function
        hash_value = 0
        prime = 31
        mod = 10**9 + 9
        for char in key:
            hash_value = (hash_value * prime + ord(char)) % mod
        return hash_value

    def put(self, key, value):
        index = self.hash_code(key) % self.size
        bucket = self.buckets[index]

        for entry in bucket:
            if entry.key == key:
                entry.value = value  # Update
                return
        bucket.append(Entry(key, value))  # Insert new

    def get(self, key):
        index = self.hash_code(key) % self.size
        bucket = self.buckets[index]

        for entry in bucket:
            if entry.key == key:
                return entry.value
        return None

    def remove(self, key):
        index = self.hash_code(key) % self.size
        bucket = self.buckets[index]

        for i, entry in enumerate(bucket):
            if entry.key == key:
                del bucket[i]
                return True  # Successfully removed
        return False  # Key not found

# Example usage:
if __name__ == "__main__":
    ht = HashTable()
    ht.put("apple", 100)
    ht.put("grape", 250)
    ht.put("cat", 200)

    print(ht.get("apple"))    # Output: 100
    print(ht.remove("apple")) # Output: True
    print(ht.get("apple"))    # Output: None
