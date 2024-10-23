import module_a as m

print("Welcome to Car Renting Service Portal")

car= m.Cars()
car.create_car()
while True:
    print("1. Customer Signin")
    print("2. Customer Signup")
    print("3. Add Car")
    print("4. Exit")

    choice = input("Enter your choice")

    if choice == '1':
        car.Car_processing()
    elif choice == '2':
        customer = m.Customer()
        customer.create_customer()
    elif choice == '3':
        print("Please add the cars by hardcoding into the array 'all_cars' present inside the code")
    elif choice == '4':
        quit()
    else:
        print("Invalid choice")
