import database
from database import *
import os

# Load all cars from the JSON file
loaded_cars = Database.load_all_cars("car_list.json")
loaded_customers = Database.load_all_customers("customer_list.json")

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
def vehicle_menu():
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

        if choice in allowed:
            # Perform actions based on user choice
            match choice.lower():
                case "s":
                    list_cars(loaded_cars)  # Call function to list all cars
                case "a":
                    Database.add_car(
                        input("Brand > "), int(input("Mileage > ")), input("Model > "), input("Color > "),
                        int(input("Rental price > ")), input("Location > "), int(input("Year > ")),
                        car_id_generator(loaded_cars), loaded_cars
                    )  # Call function to add a new car
                case "i":
                    show_car_by_id(loaded_cars, input("Please state the ID of the car you want to search: "))
                    # Call function to show a specific car by its ID
                case "d":
                    Database.delete_car_by_id(input("Please state the ID of the car you want to delete: "), loaded_cars)
                    # Call function to delete a car by its ID
                case "x":
                    break  # Exit the vehicle menu
        else:
            print("Invalid input. Please try again.")


# Function to display the customer management menu
def customer_menu():
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
            case "r":
                rent_out_car()  # Call function to rent out a car
            case "c":
                check_in_car()  # Call function to check in a car
            case "x":
                break  # Exit the customer menu


def add_new_customer():
    print(CUSTOMER_MENU_ART)
    name = input("Name: ")
    age = int(input("Age: "))
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
        elif int(choice) in customer_ids:
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
            elif int(choice) in car_ids:
                selected_car = get_car_by_id(loaded_cars, int(choice))

                # Check if the car is already rented
                if selected_car.check_availability():
                    print("This car is already rented.")
                else:
                    # Assign the car to the customer and mark it as rented
                    selected_customer.set_rented_car(choice)
                    selected_car.set_rented()
                    print("The car has been given to the customer")
                    print("------------------------------------")
                    break
            else:
                print("Invalid car ID.")
        else:
            print("Invalid customer ID.")


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
        elif int(choice) in customer_ids:
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
            elif int(choice) in car_ids:
                selected_car = get_car_by_id(loaded_cars, int(choice))

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
        else:
            print("Invalid customer ID.")


# Call the main menu function to start the program
main_choice = main_menu()

while main_choice.lower() != "x":
    if main_choice.lower() == "v":
        vehicle_menu()
    elif main_choice.lower() == "c":
        customer_menu()

    main_choice = main_menu()