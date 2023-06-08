from database import Database

# Load all cars from the JSON file
loaded_cars = Database.load_all_cars("car_rental.json")

while True:

    print("What do you want to do?")
    print("- S to show all cars")
    print("- A to add a new car")
    print("- D to delete a car by its ID")
    print("- C to close the program")

    choice = input("> ")

    if choice.lower() == "s":
        for car in loaded_cars:
            print("Brand:", car.get_brand())
            print("Year:", car.get_year())
            print("ID:", car.get_id())

    elif choice.lower() == "a":
        Database.add_car(
            input("Brand > "), input("Mileage > "), input("Model > "), input("Color > "),
            input("Rental price > "), input("Location > "), input("Year > "), input("ID > "),
            loaded_cars
        )

    elif choice.lower() == "d":
        Database.delete_car_by_id(input("Please state the ID of the car you want to delete: "), loaded_cars)

    elif choice.lower() == "c":
        # Save all cars to the JSON file before exiting
        Database.save_all_cars("car_rental.json", loaded_cars)
        print("The data has been saved")
        break
