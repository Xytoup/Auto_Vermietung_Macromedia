class Customer:
    def __init__(self, name, age, id, rented_car=None):
        self.name = name
        self.age = age
        self.id = id
        self.rented_car = rented_car

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_rented_car(self):
        return self.rented_car

    def set_rented_car(self, rented_car):
        self.rented_car = rented_car

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "id": self.id,
            "rented_car": self.rented_car
        }
