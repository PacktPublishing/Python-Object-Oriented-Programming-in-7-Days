# Immutable Types
# Strings are objects

myString = "My String"
print("myString type is ", type(myString)," and ID is ", id(myString))

myTuple = (10, 'My String', 12)
print("myTuple type is ", type(myTuple), " and ID is ", id(myTuple))

myInt = 10
print("myInt type is ", type(myInt), " and ID is ", id(myInt))

myNewInt = myInt
print("myNewInt is type ", type(myNewInt), " and ID is ", id(myNewInt))

myInt = 20
print("Value of myInt now is ", myInt, " and ID is ", id(myInt))

print("Value of myNewInt is ", myNewInt, " and ID is ", id(myNewInt))