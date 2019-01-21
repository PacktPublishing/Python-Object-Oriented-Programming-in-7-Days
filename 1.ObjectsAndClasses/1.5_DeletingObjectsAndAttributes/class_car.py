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
print(dir(a))

#delattr(a,"num_of_wheels")
#print(a.num_of_wheels)

del a.num_of_wheels
print(a.num_of_wheels)