
############################################
print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################



class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """"""

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        """"""

        print(f"{self.restaurant_name.title()}")
        print(f"{self.cuisine_type.title()}")
    
    
    def open_restaurant(self):
        """"""

        print("The restaurant is open.")


restaurant = Restaurant('Al khateeb', 'delivery')
restaurant2 = Restaurant('Al qarmooshi', 'delevery')
restaurant3 = Restaurant('Hatabtab', 'delevery')

restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()




############################################
print('\n')  # Spaces for convention only!
############################################
