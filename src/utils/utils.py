import random
import string


def random_string_and_number():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
