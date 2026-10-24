"""
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out
"""



expenses = [2200, 2350, 2600, 2130, 2190]

# 1.1 In Feb, how many dollars you spent extra compare to January?

extra_1_2 = abs(expenses[0] - expenses[1])
print(f"1.1: {extra_1_2}")

# 1.2 Find out your total expense in first quarter (first three months) of the year.

total_first_quarter = 0
for i in range(3):
    total_first_quarter += expenses[i]

print(f"1.2: {total_first_quarter}")

# 1.3 Find out if you spent exactly 2000 dollars in any month
flag = False
for i in range(len(expenses)):
    if expenses[i] == 2000:
        flag = True
        break

# if flag:
#     print("Yes")
# else:
#     print("No")

print(f"1.3: {"Yes" if flag else "No"}")

# 1.4 June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

expenses.append(1980)
print(f"1.4: {expenses}")

# 1.5 You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list
#  based on this
expenses[3] -= 200
# print(expenses)

print(f"1.5: {expenses}")