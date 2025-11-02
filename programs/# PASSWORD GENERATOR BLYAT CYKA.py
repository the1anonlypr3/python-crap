import random
import string

# Ask for password length
password_len = int(input("How many characters? \n"))
print(f"Password length: {password_len} characters")

# Build character pool
character_pool = ""

# Ask if user wants uppercase letters
def password_uppercase_letters():
    uppercase_lets = input("Include uppercase letters? (y/n): \n").lower()
    if uppercase_lets in ["y", "yes"]:
        return string.ascii_uppercase, "yes"
    else:
        return "", "no"

# Ask if user wants numbers
def password_numbers():
    numbers = input("Include numbers? (y/n): \n").lower()
    if numbers in ["y", "yes"]:
        return string.digits, "yes"
    else:
        return "", "no"

# Ask if user wants lowercase letters
def password_lowercase_letters():
    lowercase_lets = input("Include lowercase letters? (y/n): \n").lower()
    if lowercase_lets in ["y", "yes"]:
        return string.ascii_lowercase, "yes"
    else:
        return "", "no"

# Ask if user wants special characters
def password_special_chars():
    symbols = input("Include special characters? (y/n): \n").lower()
    if symbols in ["y", "yes"]:
        return string.punctuation, "yes"
    else:
        return "", "no"

# Call functions, get responses
uppers, includeduppers = password_uppercase_letters()
digits, includednumbers = password_numbers()
lowers, includedlowers = password_lowercase_letters()
special_chars, includedsymbols = password_special_chars()

# Add chosen character sets to the pool
character_pool += uppers + digits + lowers + special_chars

# Show user choices
print(f"Uppercase letters: {includeduppers}")
print(f"Numbers: {includednumbers}")
print(f"Lowercase letters: {includedlowers}")
print(f"Special characters: {includedsymbols}")

# Final check
if not character_pool:
    print("\nError: No character types selected. Cannot generate password.")
else:
    # Generate password
    password = [random.choice(character_pool) for _ in range(password_len)]
    print("\nGenerated password:", ''.join(password))

