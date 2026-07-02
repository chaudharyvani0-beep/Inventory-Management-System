def get_positive_integer(message):
    while True:
        try:
            value = int(input(message))

            if value >= 0:
                return value

            print("Value cannot be negative.")

        except ValueError:
            print("Please enter a valid number.")