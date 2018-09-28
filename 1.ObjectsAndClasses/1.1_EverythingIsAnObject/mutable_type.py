# Mutable Types
# Lists are objects

myList = [10, 'My string', 12]
print("List is type ", type(myList))

# Dictionaries are objects
numberDict = {1: 'one', 2: 'two'}
print("Dictionary is type ", type(numberDict))

# Lets focus on what is mutable
z = myList

print(z)
print(myList)

# Lets change the value of x by adding another element
# Check if z also has changed?

myList.append(14)

print(z)
print(myList)

# the list object does have mutating methods, so it can be changed.