from menu import *

while True:
    choice = main_menu().lower()

    if choice == "v":
        vehicle_menu(loaded_cars)  # Pass the loaded cars as an argument
    elif choice == "c":
        customer_menu(loaded_customers)  # Pass the loaded customers as an argument
    elif choice == "x":
        database.save_all(loaded_cars, loaded_customers)
        break
