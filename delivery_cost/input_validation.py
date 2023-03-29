def validate_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))

            if value <= 0:
                raise ValueError("Invalid input. Value must be more than 0")

            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")


def validate_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))

            if value <= 0:
                raise ValueError("Invalid input. Value must be more than 0")

            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def validate_string_input(prompt):
    while True:
        value = input(prompt)
        if value.strip() == "":
            print("Invalid input. Please enter a non-empty string.")
        else:
            return value.strip()


def validate_int(value):
    try:
        value = int(value)

        if value <= 0:
            return "Invalid input. Value must be more than 0"

        return value
    except ValueError:
        return "Invalid input. Not an integer."


def validate_float(value):
    try:
        value = float(value)

        if value <= 0:
            return "Invalid input. Value must be more than 0"

        return value
    except ValueError:
        return "Invalid input. Not a float."


def validate_str(value):
    value = str(value)
    if value.strip() == "":
        return "Invalid input. Empty string given."
    else:
        return value.strip()
