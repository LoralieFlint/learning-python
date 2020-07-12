# lists in python are arrays in javascript
friends = ["Jess", "Jess", "Jess", "Hope", "Lexi", "Tattoo Girl"]

# lists can hold stings numbers and booleans
friends2 = ["Jess", 1, True]

# index starts at 0 just like javascript
print(friends[0])

# targeting index by negative numbers
# starts at the last index of list
# returnsTattoo Girl
print(friends[-1])

# accessing portions of a list
# this will return index of 1 and the rest of the list
print(friends[1:])

# accessing a range of items in a list
# returns names from index 1 and two stops at 3 not returning it
print(friends[1:3])

# modify an item in A list
friends[1] = "Hopey"
print(friends)