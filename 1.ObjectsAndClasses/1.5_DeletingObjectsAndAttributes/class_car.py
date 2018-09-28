'''
Define a CarModel() class.
- Delete an attribute of a car, num_of_wheels
- Use delattr and del
'''
class CarModel:
    '''A simple class'''

    def __init__(self):
        self.num_of_wheels = 4

    def get_car_model(self):
        return("This is Ford Mustang. It has "+ str(self.num_of_wheels)+" wheels.")

a = CarModel()
print(a.num_of_wheels)
print(dir(a))

##Deleting the attribute using delattr
delattr(a,'num_of_wheels')

#Deleting the attribute using del
#del a.num_of_wheels

print(a.num_of_wheels)