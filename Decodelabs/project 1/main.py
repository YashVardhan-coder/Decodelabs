import string

def check_password_strength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)
    
    score = sum([has_upper, has_lower, has_digit, has_symbol])
    
    if length < 8:
        return "Weak (Password length must be at least 8 characters)"
    elif score == 4 and length >= 12:
        return "Very Strong (Excellent length and character diversity)"
    elif score == 4:
        return "Strong (Contains uppercase, lowercase, digits, and symbols)"
    elif score >= 2:
        return "Medium (Consider adding more character types)"
    else:
        return "Weak (Lacks character variety)"

def main():
    while True:
        password = input("Enter a password to check: ")
        result = check_password_strength(password)
        print(f"Password Strength: {result}\n")
        
        choice = input("Do you want to check another password? (Yes/No): ")
        if choice.strip().lower() != "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
