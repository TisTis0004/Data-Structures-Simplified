"""
The Scenario: Managing Store Inventory
Let's say you are managing the inventory of a small fruit stand.
Your current stock is represented by a dictionary where the keys are the fruit names and the values are the quantities.
"""

# Initial dictionary
inventory = {
    "apples": 50,
    "bananas": 120,
    "oranges": 75,
    "grapes": 30
}


# 1.1 Print the number of oranges currently in stock.

print(f"1.1 {inventory.get("oranges")} oranges in stock.")

# 1.2 A new shipment just arrived! Add 40 "pears" to your inventory.

inventory["pears"] = 40
print(f"1.2 {inventory}")

# 1.3 A customer just bought 15 apples. Update the inventory to reflect this sale.

inventory["apples"] -= 15
print(f"1.3 {inventory}")

# 1.4 Write code to check if "mangos" exist in your inventory. (Print "Yes" if they do, or "No" if they don't).

print("1.4", end=" ")

if "mangos" in inventory:
    print("Yes")
else:
    print("No")

# 1.5 Write a loop to calculate the total number of fruits you have in stock across all types.

total = 0
for k, v in inventory.items():
    print(v, k)
    total += v
print(f"1.5 {total} fruits in total")

# 1.6 The grapes went bad. Completely remove them from the dictionary.

inventory.pop("grapes")
print(f"1.6 {inventory}")