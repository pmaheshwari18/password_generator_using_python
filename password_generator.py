import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    # Get user input for password length and quantity
    length = int(input("Enter the desired password length: "))
    quantity = int(input("Enter the number of passwords to generate: "))

    # Generate and display passwords
    for _ in range(quantity):
        password = generate_password(length)
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
