class Car:
    def __init__(self, brand, mileage, model, color, rental_price, location):
        self.brand = brand
        self.mileage = mileage
        self.model = model
        self.color = color
        self.rental_price = rental_price
        self.location = location
        self.status = "available"

    def set_brand(self, brand):
        self.brand = brand

    def get_brand(self):
        return self.brand

    def set_mileage(self, mileage):
        self.mileage = int(mileage)

    def get_mileage(self):
        return self.mileage

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_rental_price(self, rental_price):
        self.rental_price = int(rental_price)

    def get_rental_price(self):
        return self.rental_price

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def set_rented(self):
        self.status = "rented"

    def set_available(self):
        self.status = "available"

    def check_availability(self):
        if self.status == "available":
            return True
        else:
            return False
    def calculate_rental_cost(self, days):
        return self.rental_price * int(days)