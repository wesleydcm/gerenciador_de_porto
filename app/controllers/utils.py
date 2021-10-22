import string
import secrets
from flask import current_app


error_messages = {
    'travel_not_found': "travel not found, please review 'travel_code'."
}


def generate_random_alphanumeric(length: int) -> str:
    """
        receives the length and generates randomly,
        an alphanumeric string with the given length
    """

    alphanumeric = string.ascii_letters + string.digits

    while True:
        random_alphanumeric = ''.join(
            secrets.choice(alphanumeric) for _ in range(length)
        )

        if (any(c.islower() for c in random_alphanumeric)
                and any(c.isupper() for c in random_alphanumeric)
                and sum(c.isdigit() for c in random_alphanumeric) >= 3):
            break

    return random_alphanumeric


def session(model, action):
    """
        receives the object and an write the action
        to "add" to add to db
        or "remove" to delete from the db
    """
    session = current_app.db.session()

    if action == "add":
        session.add(model)
        session.commit()

    elif action == "remove":
        session.delete(model)
        session.commit()

