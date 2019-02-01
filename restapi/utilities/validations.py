import re

def check_proper_email_format(email):
    """validates the email format"""
    return re.match(
        '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
        email)

def check_length_of_phone_number(phonenumber):
    return len(phonenumber) < 10 

def check_format_of_phone_number(phonenumber):
    return re.match( [0-9], phonenumber)

def check_length_of_fields(*args):
    for field in args:
        if len(field) > 30:
            return True

def check_unfilled_fields(*args):
    for field in args:
        if field == '':
            return True

def check_special_characters(user_input):
    special_characters = '$#@%&*!?'

    special_character = 0

    for character in user_input:
        if special_characters.find(character) != -1:
            special_character += 1

    if special_character >= 1:
        return True
