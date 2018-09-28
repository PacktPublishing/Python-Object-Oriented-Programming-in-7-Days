# Python has names and bindings

class Test1:
    #All local variables
    #Function Definitions
    pass

class Test2(Test1):
    pass

# a is a 'name' with the 'binding' to the 'object' created by Test1()
# Note: RHS creates an object
a = Test1()
b = Test2()

# Binding the name c to the same object a is bound to.
c = a

# Binding a name to an object doesn't change it
print("Type a is ", type(a))
print("Type b is ", type(b))
print("Type c is ", type(c))

print(Test1.__dict__)
