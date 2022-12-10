
############################################
print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################



class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type,):
        """"""

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        """"""

        print(f"{self.restaurant_name.title()}")
        print(f"{self.cuisine_type.title()}")
        print(f"{self.number_served} Customers served!")
    
    
    def open_restaurant(self):
        """"""

        print("The restaurant is open.")
        
        
    def set_number_served(self, new_number_served):
        """"""
        
        self.number_served = new_number_served
        
        
    def increment_number_served(self, incremented_number_served):
        """"""
        
        self.number_served += incremented_number_served
        


restaurant = Restaurant('Al khateeb', 'delivery')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.open_restaurant()
restaurant.describe_restaurant()

print(restaurant.number_served)
restaurant.number_served = 2
restaurant.describe_restaurant()

print(), print(),

restaurant.set_number_served(20)
print(restaurant.number_served)
restaurant.describe_restaurant()

print(), print(),

restaurant.increment_number_served(133)
restaurant.describe_restaurant()


############################################
print('\n')  # Spaces for convention only!
############################################
