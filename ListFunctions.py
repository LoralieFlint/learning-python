# LIST FUNCTIONS
lucky_numbers = [4, 8, 15, 42, 16, 23]
friends = ["Jess", "Hope", "Lexi", "Tattoo Girl"]

# adding an item to the end of a list
friends.append("Dad")
print(friends)

# inserting an item to a list
# takes 2 parameters index to insert item and item
friends.insert(1, "Kelly")
print(friends)

# remove item from list
friends.remove("Kelly")

print(friends)

# deleting last item in list
friends.pop()
print(friends)

# finding the index of an ittem in a list
print(friends.index("Jess"))

# how many multiples of a item are in a list
print(friends.count("Jess"))

# sorting a list from acending to decending or alphabetically
friends.sort()
print(friends)

# sorting a list from acending to decending or alphabetically
lucky_numbers.sort()
print(lucky_numbers)

# reversing the order of a list
lucky_numbers.reverse()
print(lucky_numbers)

# copying a list
new_friends = friends.copy()
print(new_friends)

# extending a list
# this will combine 2 lists into 1
friends.extend(lucky_numbers)
print(friends)

# to delete an entire list
friends.clear()
print(friends)