import database
from database import *
import os

loaded_cars, loaded_customers = load_all()

# Add ASCII art and styling to the main menu
MAIN_MENU_ART = """
-------------------------------------
         CAR RENTAL SYSTEM
-------------------------------------
"""

# Add ASCII art and styling to the vehicle management menu
VEHICLE_MENU_ART = """
-------------------------------------
       VEHICLE MANAGEMENT MENU
-------------------------------------
"""

# Add ASCII art and styling to the customer management menu
CUSTOMER_MENU_ART = """
-------------------------------------
       CUSTOMER MANAGEMENT MENU
-------------------------------------
"""


# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to display the main menu
def main_menu():
    allowed = ["v", "c", "x"]
    while True:
        clear_screen()
        print(MAIN_MENU_ART)
        print("What do you want to do?")
        print("- V for vehicle management")
        print("- C for customer management")
        print("- X to close the program")
        choice = input("> ")

        if choice.lower() in allowed:
            return choice
        else:
            print("Invalid input. Please try again.")


# Function to display the vehicle management menu
def vehicle_menu(loaded_cars):
    allowed = ["s", "a", "i", "d", "x"]
    while True:
        clear_screen()
        print(VEHICLE_MENU_ART)
        print("What do you want to do?")
        print("- S to show all cars")
        print("- A to add a new car")
        print("- I to search a specific car by its ID")
        print("- D to delete a car by its ID")
        print("- X to return to the main menu")

        choice = input("> ")

        if choice.lower() in allowed:
            # Perform actions based on user choice
            match choice.lower():
                case "s":
                    list_cars(loaded_cars)  # Call function to list all cars
                case "a":
                    print("What type of car do you want to add?")
                    print("- N for normal car")
                    print("- E for electric car")

                    while True:
                        car_type = input("> ")

                        if car_type.lower() == "n":
                            # Add a normal car
                            brand = input("Brand > ")
                            model = input("Model > ")
                            while True:
                                try:
                                    mileage = int(input("Mileage > "))
                                    break
                                except ValueError:
                                    print("Please enter a valid number!")
                            color = input("Color > ")
                            while True:
                                try:
                                    year = int(input("Year > "))
                                    break
                                except ValueError:
                                    print("Please enter a valid number!")
                            while True:
                                try:
                                    rental_price = int(input("Rental price > "))
                                    break
                                except ValueError:
                                    print("Please enter a valid number!")
                            location = input("Location > ")

                            car_id = car_id_generator(loaded_cars)
                            new_car = Car(brand, mileage, model, color, rental_price, location, year, car_id)
                            loaded_cars.append(new_car)

                            print("Normal car added successfully!")
                            print("------------------------------------")
                            break

                        elif car_type.lower() == "e":
                            # Add an electric car
                            brand = input("Brand > ")
                            model = input("Model > ")
                            while True:
                                try:
                                    mileage = int(input("Mileage > "))
                                    break
                                except ValueError:
                                    print("Please enter a valid number!")
                            color = input("Color > ")
                            while True:
                                try:
                                    year = int(input("Year > "))
                                    break
                                except ValueError:
                                    print("Please enter a valid number!")
                            while True:
                                try:
                                    rental_price = int(input("Rental price > "))
                                    break
                                except ValueError:
                                    print("Please enter a valid number!")
                            location = input("Location > ")
                            while True:
                                try:
                                    battery_capacity = int(input("Battery capacity > "))
                                    break
                                except ValueError:
                                    print("Please enter a valid number!")

                            car_id = car_id_generator(loaded_cars)
                            new_car = ElectricCar(brand, mileage, model, color, rental_price, location, year, car_id,
                                                  battery_capacity)
                            loaded_cars.append(new_car)

                            print("Electric car added successfully!")
                            print("------------------------------------")
                            break

                        else:
                            print("Invalid input. Please try again.")
                case "i":
                    try:
                        car_id = input("Please state the ID of the car you want to search: ")
                        if len(car_id) != 4:
                            raise ValueError("Invalid ID. Please enter a 4-digit ID.")

                        show_car_by_id(loaded_cars, car_id)
                        # Call function to show a specific car by its ID
                        input("press anything")
                    except ValueError as e:
                        print(str(e))
                        input("press anything")

                case "d":
                    try:
                        car_id = input("Please state the ID of the car you want to delete: ")
                        if len(car_id) != 4:
                            raise ValueError("Invalid ID. Please enter a 4-digit ID.")

                        Database.delete_car_by_id(car_id, loaded_cars)
                        # Call function to delete a car by its ID
                        input("press anything")
                    except ValueError as e:
                        print(str(e))
                        input("press anything")

                case "x":
                    break  # Exit the vehicle menu
        else:
            print("Invalid input. Please try again.")


# Function to display the customer management menu
def customer_menu(loaded_customers):
    allowed = ["s", "a", "r", "x", "c"]
    while True:
        clear_screen()
        print(CUSTOMER_MENU_ART)
        print("What do you want to do?")
        print("- S to show all customers")
        print("- A to add a new customer")
        print("- R to rent out a car")
        print("- C to check a car back in")
        print("- X to return to the main menu")

        choice = input("> ")

        if choice.lower() not in allowed:
            print("Invalid input. Please try again.")

        # Perform actions based on user choice
        match choice.lower():
            case "s":
                list_customers(loaded_customers)  # Call function to list all customers
            case "a":
                add_new_customer()  # Call function to add a new customer
                input("press anything")
            case "r":
                rent_out_car()  # Call function to rent out a car
                input("press anything")
            case "c":
                check_in_car()  # Call function to check in a car
                input("press anything")
            case "x":
                break  # Exit the customer menu


def add_new_customer():
    print(CUSTOMER_MENU_ART)
    name = input("Name: ")
    while True:
        try:
            age = int(input("Age: "))
            break
        except ValueError:
            print("Please enter a valid number!")
    customer_id = customer_id_generator(loaded_customers)
    Database.add_customer(name, age, customer_id, loaded_customers)  # Call function to add a new customer


def rent_out_car():
    # Get the list of customer IDs
    customer_ids = Database.get_all_customer_ids(loaded_customers)

    # Get the list of car IDs
    car_ids = database.get_all_car_ids(loaded_cars)

    # ASCII art for the rent out car prompt
    RENT_OUT_CAR_PROMPT_ART = """
-------------------------------------
         RENT OUT A CAR
-------------------------------------
"""

    while True:
        print(RENT_OUT_CAR_PROMPT_ART)
        print("Quick customer ID list:", customer_ids)

        # Prompt the user to enter the customer ID or return to the menu
        choice = input("Enter the customer ID or press X to return to the menu: ")

        if choice.lower() == "x":
            break

        # Check if the entered customer ID is valid
        try:
            customer_id = int(choice)
            if len(choice) != 4:
                raise ValueError("Invalid customer ID. Please enter a 4-digit ID.")

            if customer_id in customer_ids:
                print(f"Customer with ID {choice} selected")
                selected_customer = get_customer_by_id(loaded_customers, choice)

                # Check if the customer already has a car rented
                if selected_customer.get_rented_car() is not None:
                    print("This customer already has a car rented.")
                    print("------------------------------------")
                    break

                print("Quick car ID list:", car_ids)

                # Prompt the user to enter the car's ID or return to the menu
                choice = input("Enter the car's ID or press X to return to the menu: ")

                if choice.lower() == "x":
                    break

                # Check if the entered car ID is valid
                try:
                    car_id = int(choice)
                    if len(choice) != 4:
                        raise ValueError("Invalid car ID. Please enter a 4-digit ID.")

                    if car_id in car_ids:
                        selected_car = get_car_by_id(loaded_cars, car_id)

                        # Check if the car is already rented
                        if selected_car.check_availability():
                            print("This car is already rented out.")
                        else:
                            # Assign the car to the customer and mark it as rented
                            selected_customer.set_rented_car(choice)
                            selected_car.set_rented()
                            print("The car has been given to the customer")
                            print("------------------------------------")
                            break
                    else:
                        print("Invalid car ID.")
                except ValueError:
                    print("Invalid car ID. Please enter a numeric value.")
            else:
                print("Invalid customer ID.")
        except ValueError:
            print("Invalid customer ID. Please enter a numeric value.")


def check_in_car():
    # Get the list of customer IDs
    customer_ids = Database.get_all_customer_ids(loaded_customers)

    # Get the list of car IDs
    car_ids = database.get_all_car_ids(loaded_cars)

    # ASCII art for the check in car prompt
    CHECK_IN_CAR_PROMPT_ART = """
    -------------------------------------
             CHECK IN A CAR
    -------------------------------------
    """

    while True:
        print(CHECK_IN_CAR_PROMPT_ART)
        print("Quick customer ID list:", customer_ids)

        # Prompt the user to enter the customer ID or return to the menu
        choice = input("Enter the customer ID or press X to return to the menu: ")

        if choice.lower() == "x":
            break

        # Check if the entered customer ID is valid
        try:
            customer_id = int(choice)
            if len(choice) != 4:
                raise ValueError("Invalid customer ID. Please enter a 4-digit ID.")

            if customer_id in customer_ids:
                print(f"Customer with ID {choice} selected")
                selected_customer = get_customer_by_id(loaded_customers, choice)

                # Check if the customer has a rented car
                if selected_customer.get_rented_car() is None:
                    print("This customer doesn't have a car rented.")
                    print("------------------------------------")
                    break

                print("Quick car ID list:", car_ids)

                # Prompt the user to enter the car's ID or return to the menu
                choice = input("Enter the car's ID or press X to return to the menu: ")

                if choice.lower() == "x":
                    break

                # Check if the entered car ID is valid
                try:
                    car_id = int(choice)
                    if len(choice) != 4:
                        raise ValueError("Invalid car ID. Please enter a 4-digit ID.")

                    if car_id in car_ids:
                        selected_car = get_car_by_id(loaded_cars, car_id)

                        # Check if the car is currently rented
                        if not selected_car.check_availability():
                            print("This car is not currently rented.")
                        else:
                            # Perform the check-in process for the car
                            check_in(selected_customer, selected_car)
                            print("The car has been returned")
                            print("------------------------------------")
                            price_calc(selected_car)
                            print("------------------------------------")
                            print("Confirm the receipt of the payment with Y")

                            while True:
                                # Prompt the user to confirm the payment receipt
                                if input("> ").lower() == "y":
                                    print("Payment Confirmed")
                                    print("------------------------------------")
                                    break
                                else:
                                    print("Payment has not been confirmed")
                            break
                    else:
                        print("Invalid car ID.")
                except ValueError:
                    print("Invalid car ID. Please enter a numeric value.")
            else:
                print("Invalid customer ID.")
        except ValueError:
            print("Invalid customer ID. Please enter a numeric value.")
