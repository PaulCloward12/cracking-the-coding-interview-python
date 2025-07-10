#Inefficient String Concatenation (O(n²))

s = ""
for i in range(10000):
    s += str(i)
print(s[:100] + "...")  # Print first 100 characters to avoid flooding the output


# Efficient String Concatenation using list and join (O(n))

parts = []
for i in range(10000):
    parts.append(str(i))
s = ''.join(parts)
print(s[:100] + "...")  # Print first 100 characters to avoid flooding the output
