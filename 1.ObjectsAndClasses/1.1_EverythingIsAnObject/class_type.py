#  Python has names and bindings

class Test1:
    pass

class Test2(Test1):
    pass

a = Test1()
b = Test2()
c = a

print("Type a is ", type(a))
print("Type b is ", type(b))
print("Type c is ", type(c))

a.new_attribute = 1
print("Check if the attribute in a ", a.new_attribute, " exists in c to ", c.new_attribute)

print(Test1.__dict__)