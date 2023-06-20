import random
import json
import os
from car import *
from customer import Customer


def load_all():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    car_list_file = os.path.join(script_dir, "car_list.json")
    loaded_cars = Database.load_all_cars(car_list_file)

    customer_list_file = os.path.join(script_dir, "customer_list.json")
    loaded_customers = Database.load_all_customers(customer_list_file)

    return loaded_cars, loaded_customers


def save_all(loaded_cars, loaded_customers):
    script_dir = os.path.dirname(os.path.abspath(__file__))

    car_list_file = os.path.join(script_dir, "car_list.json")
    Database.save_all_cars(car_list_file, loaded_cars)

    customer_list_file = os.path.join(script_dir, "customer_list.json")
    Database.save_all_customers(customer_list_file, loaded_customers)

    print("The data has been saved")


class Database:
    @classmethod
    def save_all_cars(cls, filename, car_list):
        # Convert car objects to dictionaries
        cars = []
        for car in car_list:
            car_data = car.to_dict()
            if isinstance(car, ElectricCar):
                car_data["is_electric"] = True
                car_data["battery_capacity"] = car.get_battery_capacity()
            else:
                car_data["is_electric"] = False
                car_data["battery_capacity"] = 0
            cars.append(car_data)

        # Save the car data to a JSON file
        with open(filename, "w") as file:
            json.dump(cars, file, indent=4)

    @classmethod
    def load_all_cars(cls, filename):
        # Load car data from the JSON file
        with open(filename, "r") as file:
            cars_data = json.load(file)

        car_list = []
        # Create car objects from the loaded data and add them to the car list
        for car in cars_data:
            if car["is_electric"]:
                car_obj = ElectricCar(
                    brand=car["brand"],
                    mileage=car["mileage"],
                    model=car["model"],
                    color=car["color"],
                    rental_price=car["rental_price"],
                    location=car["location"],
                    year=car["year"],
                    id=car["id"],
                    status=car["status"],
                    battery_capacity=car["battery_capacity"]
                )
            else:
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

    @staticmethod
    def delete_car_by_id(car_id, car_list):
        for car in car_list:
            if car.get_id() == int(car_id):
                car_list.remove(car)
                print(f"Car with ID '{car_id}' has been deleted.")
                break
        else:
            print(f"Car with ID '{car_id}' not found.")

    @classmethod
    def add_car(cls, brand, mileage, model, color, rental_price, location, year, id, car_list, status="available",
                is_electric=False, battery_capacity=0):
        # Create a new car object
        if is_electric:
            new_car = ElectricCar(brand, mileage, model, color, rental_price, location, year, id, status,
                                  battery_capacity)
        else:
            new_car = Car(brand, mileage, model, color, rental_price, location, year, id, status)
        # Add the new car to the car list
        car_list.append(new_car)
        print("New car added successfully.")

    @staticmethod
    def save_all_customers(filename, customer_list):
        customers = [customer.to_dict() for customer in customer_list]
        with open(filename, "w") as file:
            json.dump(customers, file, indent=4)

    @staticmethod
    def load_all_customers(filename):
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

    @staticmethod
    def add_customer(name, age, id, customer_list):
        new_customer = Customer(name, age, id)
        customer_list.append(new_customer)
        print("New customer added successfully.")

    @staticmethod
    def get_all_customer_ids(customer_list):
        return [customer.id for customer in customer_list]



def list_cars(loaded_cars):
    # Display information for each car in the loaded car list
    for car in loaded_cars:
        print("------------------------------------")
        print("Brand:", car.get_brand())
        print("Model: ", car.get_model())
        print("Year:", car.get_year())
        print("ID:", car.get_id())
        print("------------------------------------")
    input("press anything")


def list_customers(customer_list):
    # Display information for each customer in the customer list
    for customer in customer_list:
        print("------------------------------------")
        print("Name:", customer.get_name())
        print("Age:", customer.get_age())
        print("ID:", customer.get_id())
        print("Car ID:", customer.get_rented_car())
        print("------------------------------------")
    input("press anything")


def get_customer_by_id(customer_list, customer_id):
    # Find the customer with the given ID in the customer list
    for customer in customer_list:
        if str(customer.get_id()) == str(customer_id):
            return customer
    # If no customer with the given ID is found
    print("Customer with ID {} not found.".format(customer_id))
    return None


def show_car_by_id(loaded_cars, car_id):
    # Find the car with the given ID in the loaded car list
    for car in loaded_cars:
        if car.get_id() == int(car_id):
            # Display car information
            print("------------------------------------")
            print("Brand:", car.get_brand())
            print("Model: ", car.get_model())
            print("Year: ", car.get_year())
            print("Mileage: ", car.get_mileage())
            print("Color: ", car.get_color())
            print("1 day rental price: ", car.get_rental_price(), "€")
            print("Location: ", car.get_location())
            print("ID: ", car.get_id())
            print("Status: ", car.get_status())
            print("------------------------------------")
            return  # Exit the function if car ID is found

    # If no car with the given ID is found
    print("Car with ID", car_id, "not found.")


def get_all_car_ids(car_list):
    # Get a list of all car IDs
    return [car.get_id() for car in car_list]


def get_car_by_id(car_list, car_id):
    # Find the car with the given ID in the car list
    for car in car_list:
        if car.get_id() == car_id:
            return car
    # If no car with the given ID is found
    return None


def check_in(customer, car):
    # Set the rented car for the customer to None
    customer.set_rented_car(None)
    # Set the car's status to available
    car.set_available()


def price_calc(car):
    # Calculate the outstanding amount for renting the car
    print("How many days did the customer rent the car?")
    days = int(input("> "))
    print(f"Outstanding amount: {days * car.get_rental_price()}€")


def car_id_generator(car_list):
    # Generate a random car ID and check if it is already in use
    new_id = random.randint(1000, 9999)
    existing_ids = [car.get_id() for car in car_list]

    if new_id in existing_ids:
        # If the generated ID is already in use, generate a new ID recursively
        return car_id_generator(car_list)
    else:
        # If the generated ID is unique, return it
        return new_id


def customer_id_generator(customer_list):
    # Generate a random customer ID and check if it is already in use
    new_id = random.randint(1000, 9999)
    existing_ids = [customer.id for customer in customer_list]

    if new_id in existing_ids:
        # If the generated ID is already in use, generate a new ID recursively
        return customer_id_generator(customer_list)
    else:
        # If the generated ID is unique, return it
        return new_id
