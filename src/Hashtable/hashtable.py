# Dict is hashtable
hashtable = {
    "name":"Tariq",
    "Level":5,
    "Country":"Jordan",
    "is_retired":False
}

# We want to create something like this dict

class HashTable:
    def __init__(self, size = 5) -> None:
        self.size = size
        # a hash table is an actual list of pairs with the key + value
        self.table = [None] * size # [None, None, None, None, None]

        # we will change the constructure later on
    
    def put(self, key, value):
        
        self.table.append(tuple([key, value]))


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

    h1.put("Name", "Fares") 

    h1.display_table()