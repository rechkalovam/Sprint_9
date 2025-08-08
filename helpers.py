import random
import string


class HelpersMethods:
    @staticmethod
    def generate_user_data():
        first_name = (''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(6, 8)))).capitalize()
        last_name = (''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(6, 8)))).capitalize()
        email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + '@example.ru'
        username = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(6, 8)))
        password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(random.randint(8, 10)))
        return {
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
            "email": email,
            "password": password
        }