from menu import *

while True:

    match main_menu().lower():
        case "v":
            vehicle_menu()

        case "c":
            customer_menu()

        case "x":
            # Save all cars to the JSON file before exiting
            Database.save_all_cars("car_list.json", loaded_cars)
            Database.save_all_customers("customer_list.json", loaded_customers)
            print("The data has been saved")
            break
