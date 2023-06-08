from database import *

# Load all cars from the JSON file
loaded_cars = Database.load_all_cars("car_rental.json")

while True:

    print("what do you want to do?")
    print("- S to show all cars")
    print("- D to delete a car by it´s ID")
    print("- C to close the program")

    choice = input("> ")

    match choice.lower():
        case "s":
            for car in loaded_cars:
                print("Brand:", car.get_brand())
                print("Year:", car.get_year())
                print("ID", car.get_id())

        case "d":
            delete_car_by_id(input("Please state the ID of the car you want to delete: "), loaded_cars)

        case "c":
            # Save all cars to the JSON file before exiting
            Database.save_all_cars("car_rental.json", loaded_cars)
            print("The data has been saved")
            break