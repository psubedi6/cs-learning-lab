class InvalidAgeError(Exception):
    pass
def validate_age(age):
    if age<0:
        raise InvalidAgeError()