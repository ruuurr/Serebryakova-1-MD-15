class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"название ресторана: {self.restaurant_name}")
        print(f"тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"ресторан {self.restaurant_name} открыт")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print("вкусы мороженого:")
        for flavor in self.flavors:
            print(f"- {flavor}")


ice_cream_stand = IceCreamStand("sweet treats", "dessert", ["ванильное", "шоколадное", "клубничное"])

ice_cream_stand.display_flavors()