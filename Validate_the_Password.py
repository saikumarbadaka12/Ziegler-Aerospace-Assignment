def validate_password(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in '_@$' for char in password):
        return False
    return True

# Test
password = input("Enter password: ")
if validate_password(password):
    print("Password is safe")
else:
    print("Password does not meet the criteria")
