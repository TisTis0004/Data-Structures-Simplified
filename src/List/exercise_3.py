"""
Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
"""

def create_odd_list(max_num:int) -> list:
    odd_list = [x for x in range(1, max_num+1) if x % 2 == 1]

    return odd_list


if __name__ == "__main__":
    max_num = int(input("Enter the max number for the odd list: "))
    odd_list = create_odd_list(max_num)

    print(f"The odd list for max number: {max_num} is:\n{odd_list}")