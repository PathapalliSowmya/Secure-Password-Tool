import string
import secrets


def generate_password():
    print("-----Generate Password----")

    length = int(input("Enter password length(8-50): "))

    while True:

        if length < 8 or length > 50:
            print("Please enter a length between 8 and 50.")
            break

        upper_case = input("Include uppercase letters? (y/n): ")
        lower_case = input("Include lowercase letters? (y/n): ")
        numbers = input("Include numbers? (y/n): ")
        special_characters = input("Include special characters? (y/n): ")

        if upper_case == 'n' and lower_case == 'n' and numbers == 'n' and special_characters == 'n':
            print("You must select at least one character type.")
            return

        else:
            characters = ""

            if upper_case == 'y':
                characters += string.ascii_uppercase

            if lower_case == 'y':
                characters += string.ascii_lowercase

            if numbers == 'y':
                characters += string.digits

            if special_characters == 'y':
                characters += string.punctuation

            if not characters:
                print("You must select at least one character type.")
                return

            password = ''.join(
                secrets.choice(characters) for i in range(length)
            )

            print("Generated Password")
            print(password)

            check_password_strength(password)
            return


def check_password_strength(password=None):
    print("---Password Strength Checker---")

    if password is None:
        password = input("Enter Password to check: ")

    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")

    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Add lowercase letters")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Add numbers")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        suggestions.append("Add special character")

    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "VERY STRONG"

    print(f"\nStrength: {strength}")

    if suggestions:
        print("Suggestions")
        for suggestion in suggestions:
            print("-", suggestion)


def main():
    while True:
        print("======================")
        print(" SECURE PASSWORD TOOL")
        print("======================")
        print("1. Generate Password")
        print("2. Check Password Strength")
        print("3. Exit")

        choice = input("Enter your Choice: ")

        if choice == '1':
            generate_password()

        elif choice == '2':
            check_password_strength()

        elif choice == '3':
            print("Thankyou for using password_tool")
            break

        else:
            print("Invalid choice... Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()