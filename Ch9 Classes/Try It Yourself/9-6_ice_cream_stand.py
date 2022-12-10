
############################################
print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################


class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type, ):
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


class IceCreamStand(Restaurant):
    """"""
    
    def __init__(self, restaurant_name, cuisine_type, ):
        """"""
        
        super().__init__(restaurant_name, cuisine_type, )
        self.flavors = ['apple', 'banana', 'black raspberry']


    def print_flavors(self):
        """"""
         
        print(f"We have the following flavors:")
        for flavor in self.flavors:
            print(flavor)


restaurant = Restaurant('al khateeb', 'delivery')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)


restaurant.open_restaurant()
restaurant.describe_restaurant()


print(), print(),

flavors = IceCreamStand('al tawoheed', 'delivery')
print(flavors.print_flavors())




############################################
print('\n')  # Spaces for convention only!
############################################
