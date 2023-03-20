# Retrieve the first recurring digit

# Breakdown:

# 1. Create a list with type of int and some duplicate integers
# 2. Convert it into hashes to make the search complexity as O(1) / or if iterating through arrays it will result in O(n)
# 2.1 -> Store hash in key and list values in value
# 3. Iterate through the lists and check the condition if any element met their respective integer (FIFO).
# 4. Print the recurred integer

import hashlib
lists = ["He", "Hi", "Hello", "He", "Hi", "Data"]

store = []

def first_recurrence(lists):
    for items in lists: # Hashing through iteration not possible with int type such as using range or len
        data = items.encode('utf-8')
        alg = hashlib.sha1(data)
        hashed = alg.hexdigest()
        store_hash = {
            'key': hashed,
            'value': items
        }
        if lists.count(items) > 1:
            store.append(store_hash)
            get_key = store_hash.get('key')
            print(f'The key is: {get_key}')
            print(f'The key of first recurred int is {get_key} and the value is {items}')
            break

first_recurrence(lists)

