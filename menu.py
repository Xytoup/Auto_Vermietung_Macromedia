import database
from database import *
from customer import *
from car import *

# Load all cars from the JSON file
loaded_cars = Database.load_all_cars("car_list.json")
loaded_customers = Database.load_all_customers("customer_list.json")


def main_menu():
    allowed = ["v", "c", "x"]
    while True:
        print("What do you want to do?")
        print("- V for vehicle management")
        print("- C for customer management")
        print("- X to close the program")
        choice = input("> ")

        if choice.lower() in allowed:
            return choice
        else:
            print("wrong input")


def vehicle_menu():
    allowed = ["s", "a", "i", "d", "x"]
    while True:
        print("What do you want to do?")
        print("- S to show all cars")
        print("- A to add a new car")
        print("- I to search a specific car by its ID")
        print("- D to delete a car by its ID")
        print("- x to return to the main menu")

        choice = input("> ")

        if choice in allowed:
            match choice.lower():
                case "s":
                    list_cars(loaded_cars)
                case "a":
                    Database.add_car(
                        input("Brand > "), int(input("Mileage > ")), input("Model > "), input("Color > "),
                        int(input("Rental price > ")), input("Location > "), int(input("Year > ")),
                        car_id_generator(loaded_cars), loaded_cars
                    )
                case "i":
                    show_car_by_id(loaded_cars, input("Please state the ID of the car you want to search: "))
                case "d":
                    Database.delete_car_by_id(input("Please state the ID of the car you want to delete: "), loaded_cars)
                case "x":
                    break
        else:
            print("wrong input")


def customer_menu():
    allowed = ["s", "a", "r", "x"]
    while True:
        print("What do you want to do?")
        print("- S to show all customers")
        print("- A to add a new customer")
        print("- R to rent out a car")
        print("- C to check a car back in")
        print("- x to return to the main menu")

        choice = input("> ")

        if choice.lower() not in allowed:
            print("Wrong input")

        match choice.lower():
            case "s":
                list_customers(loaded_customers)
            case "a":
                add_new_customer()
            case "r":
                rent_out_car()
            case "c":
                check_in_car()
            case "x":
                break


def add_new_customer():
    name = input("Name > ")
    age = int(input("Age > "))
    customer_id = customer_id_generator(loaded_customers)
    Database.add_customer(name, age, customer_id, loaded_customers)


def rent_out_car():
    customer_ids = Database.get_all_customer_ids(loaded_customers)
    car_ids = database.get_all_car_ids(loaded_cars)

    while True:
        print(customer_ids)
        choice = input("Enter the customer ID or press X to return to the menu: ")

        if choice.lower() == "x":
            break
        elif int(choice) in customer_ids:
            print(f"Customer with ID {choice} selected")
            selected_customer = get_customer_by_id(loaded_customers, choice)

            if selected_customer.get_rented_car() is not None:
                print("This customer already has a car rented.")
                print("------------------------------------")
                break

            print(car_ids)
            choice = input("Enter the car's ID or press X to return to the menu: ")
            if choice.lower() == "x":
                break

            elif int(choice) in car_ids:
                selected_car = get_car_by_id(loaded_cars, int(choice))
                if selected_car.check_availability():
                    print("This car is already rented.")
                else:
                    selected_customer.set_rented_car(choice)
                    selected_car.set_rented()
                    break
            else:
                print("Invalid car ID.")
        else:
            print("Invalid customer ID.")


def check_in_car():
    customer_ids = Database.get_all_customer_ids(loaded_customers)
    car_ids = database.get_all_car_ids(loaded_cars)

    while True:
        print(customer_ids)
        choice = input("Enter the customer ID or press X to return to the menu: ")

        if choice.lower() == "x":
            break
        elif int(choice) in customer_ids:
            print(f"Customer with ID {choice} selected")
            selected_customer = get_customer_by_id(loaded_customers, choice)

            if selected_customer.get_rented_car() is None:
                print("This customer doesn't have a car rented.")
                print("------------------------------------")
                break

            print(car_ids)
            choice = input("Enter the car's ID or press X to return to the menu: ")

            if choice.lower() == "x":
                break
            elif int(choice) in car_ids:
                selected_car = get_car_by_id(loaded_cars, int(choice))

                if not selected_car.check_availability():
                    print("This car is not currently rented.")
                else:
                    check_in(selected_customer, selected_car)
                    break
            else:
                print("Invalid car ID.")
        else:
            print("Invalid customer ID.")
