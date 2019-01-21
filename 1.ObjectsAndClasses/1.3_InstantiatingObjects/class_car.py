'''
- Create a car object, and use your method.
'''

class CarModel:
    """ A simple class"""

    num_of_wheels = 4

    def get_car_model(self):
        return ("This is Ford Mustang.")

a = CarModel()

print("Class's namespace", CarModel.__dict__)
print("Instance's namespace", a.__dict__)
print("Referencing attribute via ClassName", CarModel.num_of_wheels)
print("Referencing attribut via InstanceName",a.num_of_wheels)

#Defining a new attribute by assignment
CarModel.make = "Ford"

print("Class's namespace", CarModel.__dict__)
print("Instance's namespace", a.__dict__)
print("Referencing new attribute via ClassName",CarModel.make)
print("Referencing new attribute via InstanceName",a.make)

#Changing the attribute via classname
CarModel.num_of_wheels = 6

print("Class's namespace", CarModel.__dict__)
print("Instance's namespace", a.__dict__)
print("Referencing changed attribute via InstanceName", a.num_of_wheels)

#Changing the attribute back via InstanceName
a.num_of_wheels = 4
print("Class's namespace", CarModel.__dict__)
print("Instance's namespace", a.__dict__)