# Initialize the hash table as an empty dictionary
hash_table = {}
while True:
    key = input("Enter a key (or type 'exit' to stop): ")
    if key == 'exit':
        break

    value = input("Enter the corresponding value: ")
    hash_code = hash(key)
    if hash_code in hash_table:
        hash_table[hash_code].append((key, value))
    else:
        hash_table[hash_code] = [(key, value)]

print("Hash Table:")
for key in hash_table:
    print(f"Hash Code: {key}")
    for item in hash_table[key]:
        print(f"  {item[0]}: {item[1]}")
