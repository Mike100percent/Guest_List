
# Finished Guest_List.py
msg = '\n\tguest list'
print(msg.title())


msg = '\n\tinvite these items'
print(msg.title())



fruits = ["apple", "banana", "orange", "grape", "kiwi"]


del fruits[0]
del fruits[0]
print(fruits) 

print(f"The first fruit is: {fruits[0].title()}.")
print(f"The second fruit is: {fruits[1].title()}.")
print(f"The third fruit is: {fruits[2].title()}.")

# Add three more
msg = '\n\tAdd three more'
print(msg.title())

# Add "mango" to the beginning
fruits.insert(0, "mango")  
# Add "pineapple" to the middle
fruits.insert(len(fruits) // 2, "pineapple")  
# Add "watermelon" to the end
fruits.append("watermelon")  

print(fruits) 

for fruit in fruits:
    print(f"{fruit.title()} is invited.")

# I can only invite two
msg = '\n\tI can only invite two'
print(msg.title())


# Count the initial number of items in the list
initial_count = len(fruits)
print("Initial number of items in the list:", initial_count)

# Use .pop() until only two items are left and store the popped items
popped_items = []
while len(fruits) > 2:
    popped_item = fruits.pop()
    popped_items.append(popped_item)

# Print the final list and the popped items

print("Final list of fruits:", fruits)
print(f"{fruits[0].title()} is still invited.")
print(f"{fruits[1].title()}is still invited.")

print("Popped items:", popped_items)
print(f"{popped_items[0].title()} canceled.")
print(f"{popped_items[1].title()} canceled.")
print(f"{popped_items[2].title()} canceled.")
print("Final list of fruits:", fruits)
del fruits[0]
del fruits[0]

msg = '\n\tempty guest list'
print(msg.title())

print("Empty list of fruits:", fruits)
