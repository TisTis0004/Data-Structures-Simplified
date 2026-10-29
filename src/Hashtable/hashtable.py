# Dict is hashtable
hashtable = {
    "name":"Tariq",
    "Level":5,
    "Country":"Jordan",
    "is_retired":False
}

# We want to create something like this dict

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||IN THE LAST VERSION |||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||
"""
We were building a wrapper on the regular list without actually having the benifit of a hashtable.
The main advantage of a hashtable is its speed. if we were to look up an item in our previous implementation we would have to loop over all the items
so its a O(N).
One the other hand a hash table has O(1) on the look up...
Thanks to THE HASH FUNCTION

Simply, it takes the key and gives back an index. As simple as it can get
We use this index to put/get/delete to access a pair.

BUT there is the mighty: COLLISION ISSUE.

where two different keys might be encoded as the same index after passing through the hash function which is bad cause then the new pair will overwrite the old one.

That where COLLISION RESOLUTION STRATEGIES came in handy:

1. Chaining: Each bucket holds a list. If a collision happens, we just append to the list.
2. Open Addressing (Linear Probing): If a collision happens, we scan forward to find the next empty slot.
"""


class HashTableChaining:
    def __init__(self, size=5) -> None:
        self.size = size
        # We create a list of empty lists to hold multiple items at the same index
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        hsh = hash(key)
        index = hsh % self.size
        return index

    def put(self, key, value):
        index = self.hash_function(key)
        print(f"[Chaining] Putting '{key}': '{value}' at index {index}")
        
        # Check if key already exists to update it
        for i, kv in enumerate(self.table[index]):
            if kv[0] == key:
                self.table[index][i] = (key, value)
                print(f"  -> Updated existing key '{key}'")
                return
        
        # If no matching key, append to the chain
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        for kv in self.table[index]:
            if kv[0] == key:
                return kv[1]
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for i, kv in enumerate(self.table[index]):
            if kv[0] == key:
                print(f"[Chaining] Deleting '{key}' from index {index}")
                del self.table[index][i]
                return
        print(f"[Chaining] Key '{key}' not found.")

    def display_table(self):
        print("--- Chaining Hash Table ---")
        for i, item in enumerate(self.table):
            print(f"Index {i}: {item}")
        print("-" * 27)


class HashTableOpenAddressing:
    def __init__(self, size=5) -> None:
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        hsh = hash(key)
        index = hsh % self.size
        return index

    def put(self, key, value):
        index = self.hash_function(key)
        original_index = index
        
        print(f"[Open Addressing] Trying to put '{key}': '{value}' at index {index}")
        
        while self.table[index] is not None:
            # Update value if key already exists
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                print(f"  -> Updated existing key '{key}' at index {index}")
                return
            
            print(f"  -> Collision at index {index}! Probing next slot...")
            index = (index + 1) % self.size
            
            # Loop check to prevent infinite loops if the table is full
            if index == original_index:
                print("  -> Table is full! Cannot insert.")
                return
                
        # Empty slot found
        self.table[index] = (key, value)
        print(f"  -> Inserted '{key}' at index {index}")

    def get(self, key):
        index = self.hash_function(key)
        original_index = index
        
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == original_index:
                break
        return None

    def delete(self, key):
        index = self.hash_function(key)
        original_index = index
        
        while self.table[index] is not None:
            if self.table[index][0] == key:
                print(f"[Open Addressing] Deleting '{key}' from index {index}")
                # Note: In a production open-addressing table, you use a "Tombstone" (dummy value) 
                # here instead of None, otherwise you break the probe chain for other keys!
                self.table[index] = None 
                return
            index = (index + 1) % self.size
            if index == original_index:
                break
        print(f"[Open Addressing] Key '{key}' not found.")

    def display_table(self):
        print("--- Open Addressing Hash Table ---")
        for i, item in enumerate(self.table):
            print(f"Index {i}: {item}")
        print("-" * 34)


if __name__ == "__main__":
    # We use integers as keys in these tests to reliably trigger hash collisions.
    # If size=5: hash(10)%5 = 0, hash(15)%5 = 0, hash(20)%5 = 0.
    
    print("=========================================")
    print("       TESTING CHAINING STRATEGY         ")
    print("=========================================")
    ht_chain = HashTableChaining(size=5)
    
    ht_chain.put(10, "Apple")
    ht_chain.put(15, "Banana") # Collides with 10 (index 0)
    ht_chain.put(20, "Cherry") # Collides with 10 and 15 (index 0)
    ht_chain.put(1, "Dates")   # Goes to index 1
    
    ht_chain.display_table()
    
    print("\nUpdating an existing key (10)...")
    ht_chain.put(10, "Apricot")
    ht_chain.display_table()
    
    
    print("\n=========================================")
    print("   TESTING OPEN ADDRESSING STRATEGY      ")
    print("=========================================")
    ht_open = HashTableOpenAddressing(size=5)
    
    ht_open.put(10, "Apple")   # Goes to index 0
    ht_open.put(15, "Banana")  # Collides at 0 -> probes and lands on index 1
    ht_open.put(20, "Cherry")  # Collides at 0 -> probes 1 (taken) -> lands on index 2
    ht_open.put(1, "Dates")    # Hashes to 1, but 1 is taken by Banana -> probes and lands on index 3
    
    ht_open.display_table()
    
    print("\nUpdating an existing key (10)...")
    ht_open.put(10, "Apricot")
    ht_open.display_table()