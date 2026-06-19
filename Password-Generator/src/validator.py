def validate_length(length):
    if length <4:
        raise  ValueError("Password length should be at-least 4 characters")
    if length >50:
        raise  ValueError('Password length should be less than 50 characters')
    return True