"""
You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
"""
heros=['spider man','thor','hulk','iron man','captain america']

# 2.1 Length of the list

print(f"2.1: {len(heros)}")

# 2.2 Add 'black panther' at the end of this list

heros.append("black panther")
print(f"2.2: {heros}")

# 2.3 You realize that you need to add 'black panther' after 'hulk',
#     so remove it from the list first and then add it after 'hulk'

heros.insert(3, heros[-1])
heros.pop()
print(f"2.3: {heros}")

# 2.4 Now you don't like thor and hulk because they get angry easily :)
#     So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#     Do that with one line of code.

heros[1:3] = ["doctor strange"] # slice list off
print(f"2.4: {heros}")

# 2.5 Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

# print(dir(heros))
heros.sort()
print(f"2.5: {heros}")