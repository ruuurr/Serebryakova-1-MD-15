class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"restaurant Name: {self.restaurant_name}")
        print(f"cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"the restaurant {self.restaurant_name} is now open!")


restaurant1 = Restaurant("TOKYOCITY", "JAPANESE")
restaurant2 = Restaurant("LE FRENCH", "FRENCH")
restaurant3 = Restaurant("BITTER", "ITALIAN")


restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()