from database import Database, list_cars, show_car_by_id, id_generator

# Load all cars from the JSON file
loaded_cars = Database.load_all_cars("car_rental.json")

while True:

    print("What do you want to do?")
    print("- S to show all cars")
    print("- A to add a new car")
    print("- I to search a specific car by it´s ID")
    print("- D to delete a car by its ID")
    print("- C to close the program")

    choice = input("> ")
    match choice.lower():

        case "s":
            list_cars(loaded_cars)

        case "a":
            Database.add_car(
                input("Brand > "), int(input("Mileage > ")), input("Model > "), input("Color > "),
                int(input("Rental price > ")), input("Location > "), int(input("Year > ")), id_generator(loaded_cars),
                loaded_cars
            )

        case "i":
            show_car_by_id(loaded_cars,input("Please state the ID of the car you want to search: "))
        case "d":
            Database.delete_car_by_id(input("Please state the ID of the car you want to delete: "), loaded_cars)

        case "c":
            # Save all cars to the JSON file before exiting
            Database.save_all_cars("car_rental.json", loaded_cars)
            print("The data has been saved")
            break
