def approach_1_key(dict:dict) -> None:
    for key in dict:
        print(dict[key])

def approach_2_key_value(dict:dict) -> None:
    for k, v in dict.items(): # must add items()
        print(f"Key: {k}, Value: {v}")


def add_pair(dict:dict) -> dict:
    dict["age"] = 33
    return dict

def get_item_via_method(dict:dict) -> None:
    """Very important method to get the value with error handling if the dictionary doesn't have this key"""
    
    print(dict.get("koko"))

def remove_pair(dict:dict) -> None:
    print(f"Popped item: {dict.pop("age")}")
    print(f"Dict after popping:\n{dict}")





if __name__ == "__main__":
    emp_info = {
        "id":28,
        "name":"Samir",
        "department":"ENG",
    }
    print("Approach 1 using the key directly")
    approach_1_key(emp_info)
    print("="*10)


    print("Adding a new pair to the dictionary")
    extended_emp_info = add_pair(emp_info)
    print(extended_emp_info)
    print("="*10)

    approach_2_key_value(emp_info)
    print("="*10)

    ## dictionary length (the number of pairs / keys)
    print(f"Dictionary length: {len(emp_info)}")



    get_item_via_method(emp_info)
    print("="*10)
    remove_pair(emp_info)