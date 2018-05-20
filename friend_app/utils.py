import re


def get_valid_email(email):

    if re.match(r"[\w\.-]+@[\w\.-]+", email) is not None:
        return email
    return None