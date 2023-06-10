import random
import json
from car import Car
from customer import Customer


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

    @classmethod
    def save_all_customers(cls, filename, customer_list):
        customers = [customer.to_dict() for customer in customer_list]
        with open(filename, "w") as file:
            json.dump(customers, file, indent=4)

    @classmethod
    def load_all_customers(cls, filename):
        with open(filename, "r") as file:
            customers_data = json.load(file)

        customer_list = []
        for customer in customers_data:
            customer_obj = Customer(
                name=customer["name"],
                age=customer["age"],
                id=customer["id"],
                rented_car=customer["rented_car"]
            )
            customer_list.append(customer_obj)

        return customer_list

    @classmethod
    def add_customer(cls, name, age, id, customer_list):
        new_customer = Customer(name, age, id)
        customer_list.append(new_customer)
        print("New customer added successfully.")

    @classmethod
    def get_all_customer_ids(cls, customer_list):
        return [customer.id for customer in customer_list]


def list_cars(loaded_cars):
    for car in loaded_cars:
        print("------------------------------------")
        print("Brand:", car.get_brand())
        print("Model: ", car.get_model())
        print("Year:", car.get_year())
        print("ID:", car.get_id())
        print("------------------------------------")


def list_customers(customer_list):
    for customer in customer_list:
        print("------------------------------------")
        print("Name:", customer.get_name())
        print("Age:", customer.get_age())
        print("ID:", customer.get_id())
        print("Car ID:", customer.get_rented_car())
        print("------------------------------------")


def get_customer_by_id(customer_list, customer_id):
    for customer in customer_list:
        if str(customer.get_id()) == str(customer_id):
            return customer
    print("Customer with ID {} not found.".format(customer_id))
    return None



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
            print("ID: ", car.get_id())
            print("Status: ", car.get_status())
            print("------------------------------------")


def get_all_car_ids(car_list):
    return [car.get_id() for car in car_list]


def get_car_by_id(car_list, car_id):
    for car in car_list:
        if car.get_id() == car_id:
            return car
    return None


def check_in(customer, car):
    customer.set_rented_car(None)
    car.set_available()


def car_id_generator(car_list):
    new_id = random.randint(1000, 9999)
    existing_ids = [car.get_id() for car in car_list]

    if new_id in existing_ids:
        return car_id_generator(car_list)
    else:
        return new_id


def customer_id_generator(customer_list):
    new_id = random.randint(1000, 9999)
    existing_ids = [customer.id for customer in customer_list]

    if new_id in existing_ids:
        return customer_id_generator(customer_list)
    else:
        return new_id