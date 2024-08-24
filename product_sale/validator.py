import re


def validator(name):
    return bool(re.match(r"^[a-zA-Z0-9\s]{3,20}$", name))
