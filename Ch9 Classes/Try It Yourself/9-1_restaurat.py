
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

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)


restaurant.open_restaurant()
restaurant.describe_restaurant()





############################################
print('\n')  # Spaces for convention only!
############################################
