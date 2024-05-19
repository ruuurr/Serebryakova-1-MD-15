class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"restaurant name: {self.restaurant_name}")
        print(f"cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"the restaurant {self.restaurant_name} is now open!")


newRestaurant = Restaurant("TOKYO CITY", "JAPANESE")


print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)


newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()