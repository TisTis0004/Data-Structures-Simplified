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
"""


class HashTable:
    def __init__(self, size = 5) -> None:
        self.size = size
        # a hash table is an actual list of pairs with the key + value
        self.table = [None] * size # [None, None, None, None, None]

        # we will change the constructure later on
    


    # SUPER STAR
    def hash_function(self, key):
        hsh = hash(key)
        index = hsh % self.size
        print(f"Hash created is {hsh} and index is: {index}")
        return index


    def put(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None or index == self.hash_function(key):
            self.table[index] = tuple([key, value])


    def get(self, key):
        pass


    def delete(self, key):
        pass


    def display_table(self):
        for item in self.table:
            # print(f"{item[0]} | {item[1]}")
            print(item)

    
if __name__ == "__main__":
    h1 = HashTable()

    key = "name"
    h1.put(key, "Fares")
    h1.display_table()

    print('=' * 20)
    print(f"Now we will use the same key but change the value, so it should change existing pair rather than creating a new pair with the key: {key}")
    print('=' * 20)

    h1.put(key="name", value="Ismail")
    h1.display_table()

"""
Now this version is working fine (??)

its not.
it is true that the hash function we created gives us an index and gives the same index for the same key in O(1). BUUUUT...

There the mighty: COLLUSION ISSUE.

where two different keys might be encoded as the same index after passing through the hash function which is bad cause then the new pair will overwrite the old one.

That where COLLUSION RESOLUTION STRATIGIES came in handy
"""

    # print(h1.hash_function("koko"))
    # print(h1.hash_function("wawa"))