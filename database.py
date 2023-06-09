import random
from car import *


class Database:
    @classmethod
    def save_all_cars(cls, filename, car_list):
        cars = [car.to_dict() for car in car_list]
        with open(filename, "w") as file:
            json.dump(cars, file, indent=4)

    @classmethod
    def load_all_cars(cls, filename):
        with open(filename, "r") as file:
            cars_data = json.load(file)

        car_list = []
        for car in cars_data:
            car_obj = Car(
                brand=car["brand"],
                mileage=car["mileage"],
                model=car["model"],
                color=car["color"],
                rental_price=car["rental_price"],
                location=car["location"],
                year=car["year"],
                id=car["id"],
                status=car["status"]
            )
            car_list.append(car_obj)

        return car_list

    @classmethod
    def delete_car_by_id(cls, car_id, car_list):
        for car in car_list:
            if car.get_id() == int(car_id):
                car_list.remove(car)
                print(f"Car with ID '{car_id}' has been deleted.")
                break
        else:
            print(f"Car with ID '{car_id}' not found.")

    @classmethod
    def add_car(cls, brand, mileage, model, color, rental_price, location, year, id, car_list, status="available"):
        new_car = Car(brand, mileage, model, color, rental_price, location, year, id, status)
        car_list.append(new_car)
        print("New car added successfully.")


def list_cars(loaded_cars):
    for car in loaded_cars:
        print("------------------------------------")
        print("Brand:", car.get_brand())
        print("model", car.get_model())
        print("Year:", car.get_year())
        print("ID:", car.get_id())


def show_car_by_id(loaded_cars, car_id):
    for car in loaded_cars:
        if car.get_id() == int(car_id):
            print("------------------------------------")
            print("Brand:", car.get_brand())
            print("model: ", car.get_model())
            print("Year: ", car.get_year())
            print("Mileage: ", car.get_mileage())
            print("Color: ", car.get_color())
            print("1 day rental price ", car.get_rental_price(), "€")
            print("Location: ", car.get_location())
            print("ID:", car.get_id())


def id_generator(loaded_cars):
    new_id = random.randint(1000, 9999)
    existing_id = [car.get_id() for car in loaded_cars]

    if new_id in existing_id:
        return id_generator(loaded_cars)
    else:
        return new_id
