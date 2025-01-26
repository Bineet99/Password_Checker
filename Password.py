password = input("Enter your password: ")
if len(password) < 8:
    print("Password is too short. It should be at least 8 characters long.")
else:
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_special = True

    if not has_lower:
        print("Password must contain at least one lowercase letter.")
    if not has_upper:
        print("Password must contain at least one uppercase letter.")
    if not has_digit:
        print("Password must contain at least one number.")
    if not has_special:
        print("Password must contain at least one special character (e.g., @, #, $, %, ^, &, +, =, !).")    
    else:
        print("Password is strong!")
