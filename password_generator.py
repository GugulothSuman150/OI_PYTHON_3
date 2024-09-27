import random
import string

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    character_set = string.ascii_lowercase  # Start with lowercase letters
    
    if use_uppercase:
        character_set += string.ascii_uppercase
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation

    if len(character_set) == 0:
        raise ValueError("At least one character type must be selected.")

    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Get user input for password length
    length = int(input("Enter the desired password length: "))
    
    # Get user input for character types
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'
    
    try:
        password = generate_password(length, use_uppercase, use_numbers, use_symbols)
        print("Generated Password:", password)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
