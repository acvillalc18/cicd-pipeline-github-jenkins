# Password checking program for CI/CD pipeline testing
# python tests to check if the password checks works properly.

def check_password(password):
    if len(password) < 10:
        return False

    if not any(char.isupper() for char in password):
        return False

    if not any(char.islower() for char in password):
        return False

    if not any(char.isdigit() for char in password):
        return False

    if not any(not char.isalnum() for char in password):
        return False

    return True