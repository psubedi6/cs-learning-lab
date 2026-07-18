class InvalidEmailError(Exception):
    pass

def validate_email(email):
    if email == "" or "@" not in email:
        raise InvalidEmailError()