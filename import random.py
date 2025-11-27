import random
import string

def get_user_preferences():
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 8): "))
            if length < 8:
                print("Password length should be at least 8 characters.")
                continue
            include_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
            include_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
            include_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
            include_special = input("Include special characters? (y/n): ").strip().lower() == 'y'
            if not (include_uppercase or include_lowercase or include_digits or include_special):
                print("You must select at least one character type.")
                continue
            return length, include_uppercase, include_lowercase, include_digits, include_special
        except ValueError:
            print("Invalid input. Please enter a valid number for length.")

def generate_password(length, include_uppercase, include_lowercase, include_digits, include_special):
    character_pool = ''
    
    if include_uppercase:
        character_pool += string.ascii_uppercase
    if include_lowercase:
        character_pool += string.ascii_lowercase
    if include_digits:
        character_pool += string.digits
    if include_special:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("No character types selected for password generation.")

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    length, include_uppercase, include_lowercase, include_digits, include_special = get_user_preferences()
    
    password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_special)
    print(f"Generated Password: {password}")

if _name_ == "_main_":
    main()