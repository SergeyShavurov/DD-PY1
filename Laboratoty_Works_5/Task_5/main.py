import random
import string

def get_random_password(n = 8) -> str:
    value_pool = string.ascii_uppercase + string.ascii_lowercase + string.digits
    value_list = random.sample(value_pool, k=n)
    password = "".join(value_list)
    return password

print(get_random_password())
