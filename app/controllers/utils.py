import string
import secrets


def generate_random_alphanumeric(length):

    alphanumeric = string.ascii_letters + string.digits

    while True:
        random_alphanumeric = ''.join(secrets.choice(alphanumeric) for _ in range(length))
        
        if (any(c.islower() for c in random_alphanumeric)
                and any(c.isupper() for c in random_alphanumeric)
                and sum(c.isdigit() for c in random_alphanumeric) >= 3):
            break

    return random_alphanumeric
