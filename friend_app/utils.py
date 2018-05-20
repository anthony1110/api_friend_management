import re


def get_valid_email(email):
    if not re.match(r'[\w\.-_]+@[\w\.-_]+', email):
        return email
    return None