import random
import json
from car import Car
from customer import Customer


class Database:
    @classmethod
    def save_all_cars(cls, filename, car_list):
        # Convert car objects to dictionaries
        cars = [car.to_dict() for car in car_list]
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
        # Iterate over the car list
        for car in car_list:
            # Find the car with the matching ID
            if car.get_id() == int(car_id):
                # Remove the car from the list
                car_list.remove(car)
                print(f"Car with ID '{car_id}' has been deleted.")
                break
        else:
            # If no car with the given ID is found
            print(f"Car with ID '{car_id}' not found.")

    @classmethod
    def add_car(cls, brand, mileage, model, color, rental_price, location, year, id, car_list, status="available"):
        # Create a new car object
        new_car = Car(brand, mileage, model, color, rental_price, location, year, id, status)
        # Add the new car to the car list
        car_list.append(new_car)
        print("New car added successfully.")

    @classmethod
    def save_all_customers(cls, filename, customer_list):
        # Convert customer objects to dictionaries
        customers = [customer.to_dict() for customer in customer_list]
        # Save the customer data to a JSON file
        with open(filename, "w") as file:
            json.dump(customers, file, indent=4)

    @classmethod
    def load_all_customers(cls, filename):
        # Load customer data from the JSON file
        with open(filename, "r") as file:
            customers_data = json.load(file)

        customer_list = []
        # Create customer objects from the loaded data and add them to the customer list
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
        # Create a new customer object
        new_customer = Customer(name, age, id)
        # Add the new customer to the customer list
        customer_list.append(new_customer)
        print("New customer added successfully.")

    @classmethod
    def get_all_customer_ids(cls, customer_list):
        # Get a list of all customer IDs
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


def list_customers(customer_list):
    # Display information for each customer in the customer list
    for customer in customer_list:
        print("------------------------------------")
        print("Name:", customer.get_name())
        print("Age:", customer.get_age())
        print("ID:", customer.get_id())
        print("Car ID:", customer.get_rented_car())
        print("------------------------------------")


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
