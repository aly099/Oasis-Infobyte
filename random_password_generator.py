import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""
    
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        print("Error: Select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Random Password Generator")
    print("-------------------------")

    try:
        length = int(input("Enter the length of the password: "))
    except ValueError:
        print("Invalid input. Please enter a valid numeric value.")
        return

    if length <= 0:
        print("Invalid input. Password length must be a positive integer.")
        return

    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_letters, use_numbers, use_symbols)

    if password:
        print(f"\nYour generated password is: {password}")

if __name__ == "__main__":
    main()
