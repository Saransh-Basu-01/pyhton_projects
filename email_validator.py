import re
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    return re.fullmatch(pattern, email) is not None
email = input("Enter your email: ")
if is_valid_email(email):
    print("Email is valid, your email:", email)
else:
    print("Email is not valid.")

    