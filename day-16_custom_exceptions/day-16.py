from validators import validate_age

class InvalidAgeError(Exception):
    pass
try:
    raise InvalidAgeError()
except InvalidAgeError:
    print("Invalid age entered.")


class InvalidAgeError(Exception):
    def __init__(self):
            super().__init__("Invalid age")

class InvalidEmailError(Exception):
    def __init__(self):
            super().__init__("Invalid age")

class InvalidNameError(Exception):
    def __init__(self):
            super().__init__("Invalid age")




from validators import validate_age, InvalidAgeError
try:
    validate_age(-5)
except InvalidAgeError:
    print("Age validation failed.")