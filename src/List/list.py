# List

def approach_1_item(list:list) -> None:
    for item in list:
        print(item)

def appraoch_2_index(list:list) -> None:
    for i in range(len(list)):
        print(f"index: {i}")
        print(f"value: {list[i]}")
        print("_"*10)

def appraoch_3_while(list:list) -> None:
    counter = 0

    while counter < len(list):
        print(f"Coutner: {counter}")
        print(list[counter])

        print("_"*10)
        counter += 1


def appraoch_4_list_comprehension(list:list) -> list:
    return [x for x in list]
    # return [x for x in list if x < 500]
    # reutrn [x.id for x in list if x.startswith("a")]



# _________ Main function _________
if __name__ == "__main__":
    
    my_list = [401, 403, 404, 500]

    print("Approach 1 using the staright forward traversing through a list using for loop")
    approach_1_item(my_list)

    print("="* 30)

    print("Approuch 2 using the index via rang() and len()")
    appraoch_2_index(my_list)

    print("="* 30)

    print("Approach 3 using while loop")
    appraoch_3_while(my_list)

    print("="* 30)

    print("Approach 4 using list comprehension")
    print(appraoch_4_list_comprehension(my_list))