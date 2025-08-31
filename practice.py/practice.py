while True:
    try:
        age = int(input("How old are you? "))

        if age < 0:
            print("Please print a valid age.")
            continue
        elif age > 18:
            print("You are an adult")
        elif 13 <= age <= 17:
            print("You are a teen")
        elif age <= 12:
            print("You are a child")
        break

    except ValueError:
        print("Please print a valid age.")
