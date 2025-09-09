while True:
    try:
        number = int(input("Write a number "))

        if number % 2 == 0:
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")

    except ValueError:
        print("Please enter a valid number.")

    again = input("Check another number? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thank you for using this checker!")
        break
