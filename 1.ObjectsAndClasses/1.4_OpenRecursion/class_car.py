'''
Define a CarModel() class.
- Call the method car_model on the 'a' instance
- initialize the value num_of_wheels
- And return the string
- "This is a Ford Mustang!It has " + str(num_of_wheels) + " wheels."
'''
class CarModel:
    '''A simple class'''

    def __init__(self):
        self.num_of_wheels = 4
        print("The init method is called automatically")

    def get_car_model(self):
        return("This is a Ford Mustang!It has "+ str(self.num_of_wheels)+ " wheels.")

a = CarModel()
print(a.get_car_model())
