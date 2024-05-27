class Restaurant:
    def __init__(self, name, cuisine_type, rating):
        self.name = name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def update_rating(self, new_rating):
        self.rating = new_rating


restaurant = Restaurant("TOKYOCITY", "JAPANESE", 4.5)
print("изначальный рейтинг:", restaurant.rating)

new_rating = 4.7
restaurant.update_rating(new_rating)
print("обновленный рейтинг:", restaurant.rating)
