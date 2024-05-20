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
    def __init__(self, restaurant_name, cuisine_type, flavors, location, hours):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
        self.location = location
        self.hours = hours
        self.stick_ice_cream = []
        self.soft_ice_cream = []

    def describe_ice_cream_stand(self):
        self.describe_restaurant()
        print(f"адрес: {self.location}")
        print(f"часы работы: {self.hours}")

    def display_flavors(self):
        print("вкусы:")
        for flavor in self.flavors:
            print(f"- {flavor}")

    def add_flavor(self, flavor):
        if flavor not in self.flavors:
            self.flavors.append(flavor)
            print(f"добавить вкус: {flavor}")
        else:
            print(f"вкус {flavor} уже существует")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"удалить вкус: {flavor}")
        else:
            print(f"вкус {flavor} не найден")

    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print(f"вкус {flavor} доступен")
        else:
            print(f"вкус {flavor} недоступен")

    def add_stick_ice_cream(self, flavor):
        if flavor not in self.stick_ice_cream:
            self.stick_ice_cream.append(flavor)
            print(f"добавлен вкус фруктового льда: {flavor}")
        else:
            print(f"вкус фруктового льда {flavor} уже существует.")

    def remove_stick_ice_cream(self, flavor):
        if flavor in self.stick_ice_cream:
            self.stick_ice_cream.remove(flavor)
            print(f"удалить вкус фруктового льда : {flavor}")
        else:
            print(f"вкус фруктового льда  {flavor} не найден.")

    def display_stick_ice_cream(self):
        print("доступные вкусы фруктового льда:")
        for flavor in self.stick_ice_cream:
            print(f"- {flavor}")

    def add_soft_ice_cream(self, flavor):
        if flavor not in self.soft_ice_cream:
            self.soft_ice_cream.append(flavor)
            print(f"добавить вкус пломбира: {flavor}")
        else:
            print(f"вкус пломбира {flavor} уже существует")

    def remove_soft_ice_cream(self, flavor):
        if flavor in self.soft_ice_cream:
            self.soft_ice_cream.remove(flavor)
            print(f"удалить вкус пломбира: {flavor}")
        else:
            print(f"вкус пломбира {flavor} не найден")

    def display_soft_ice_cream(self):
        print("доступный вкус пломбира:")
        for flavor in self.soft_ice_cream:
            print(f"- {flavor}")


ice_cream_stand = IceCreamStand("TOKYOCITY", "japanese", ["ванильный", "шоколадный", "клубничный"], "лесная 545", "11:00 - 01:00")

ice_cream_stand.describe_ice_cream_stand()

ice_cream_stand.display_flavors()


ice_cream_stand.add_flavor("мятный шоколад")


ice_cream_stand.remove_flavor("ванильный")


ice_cream_stand.check_flavor("шоколадный")


ice_cream_stand.add_stick_ice_cream("манго")
ice_cream_stand.display_stick_ice_cream()


ice_cream_stand.add_soft_ice_cream("черника")
ice_cream_stand.display_soft_ice_cream()