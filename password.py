import random
import string
import pyperclip

def get_user_preferences():
    length = int(input("Enter desired password length: "))

    print("\nInclude the following in your password:")
    use_uppercase = input("Uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Digits? (y/n): ").lower() == 'y'
    use_specials = input("Special characters? (y/n): ").lower() == 'y'

    if not any([use_uppercase, use_lowercase, use_digits, use_specials]):
        print("⚠️ You must select at least one character type.")
        return get_user_preferences()

    return length, use_uppercase, use_lowercase, use_digits, use_specials

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_specials):
    char_pool = ''
    guaranteed_chars = []

    if use_uppercase:
        char_pool += string.ascii_uppercase
        guaranteed_chars.append(random.choice(string.ascii_uppercase))
    if use_lowercase:
        char_pool += string.ascii_lowercase
        guaranteed_chars.append(random.choice(string.ascii_lowercase))
    if use_digits:
        char_pool += string.digits
        guaranteed_chars.append(random.choice(string.digits))
    if use_specials:
        special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>/?"
        char_pool += special_characters
        guaranteed_chars.append(random.choice(special_characters))

    if length < len(guaranteed_chars):
        raise ValueError("Password length is too short for the selected character types.")

    password = guaranteed_chars + [random.choice(char_pool) for _ in range(length - len(guaranteed_chars))]
    random.shuffle(password)
    return ''.join(password)

def main():
    length, use_uppercase, use_lowercase, use_digits, use_specials = get_user_preferences()
    
    try:
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_specials)
        print(f"\n🔑 Generated Password: {password}")
        
        copy_choice = input("Copy to clipboard? (y/n): ").lower()
        if copy_choice == 'y':
            pyperclip.copy(password)
            print("✅ Password copied to clipboard.")
    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
