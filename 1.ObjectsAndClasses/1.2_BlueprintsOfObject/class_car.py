'''
Define a CarModel() class.
- Define an attribute of a car, num_of_wheels,
- Write one method, get_car_model(). This method should return the car model string,
  "This is a Ford Mustang!"
'''
class CarModel:
    '''A Simple Class'''
    num_of_wheels = 4

    def get_car_model():
        return("This is Ford Mustang")

a = CarModel()
CarModel.make = "Ford"
CarModel.num_of_wheels = 6

a.num_of_wheels = 4

print("Class's Namespace", CarModel.__dict__)
print("Instance's Namespace", a.__dict__)

print("Referencing Attribute via ClassName", CarModel.num_of_wheels)
print("Referencing Attribute via InstanceName", a.num_of_wheels)