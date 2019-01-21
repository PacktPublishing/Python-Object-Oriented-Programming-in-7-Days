# Mutable Types
# Lists are objects

myList = [10, "My String", 12]
print("myList type is ", type(myList), " and ID is ", id(myList))

myDictionary = {1:"one", 2:"two"}
print("myDictionary type is ", type(myDictionary), " and ID is ", id(myDictionary))

myNewList = myList
print("myNewList type is ", type(myNewList), " and ID is ", id(myNewList))

myList.append(14)
print("Value of myList now is ", myList, " and ID is ", id(myList))
print("Value of myNewList is ", myNewList, " and ID is ", id(myNewList))
