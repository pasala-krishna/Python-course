import re

def calculate_password_strength(username, password):
    # Criteria weights (adjust as needed)
    length_weight = 2
    uppercase_weight = 2
    lowercase_weight = 2
    digit_weight = 2
    special_char_weight = 3
    username_similarity_weight = -2

    score = 0

    # Length check
    if len(password) >= 8:
        score += length_weight

    # Uppercase letter check
    if re.search(r'[A-Z]', password):
        score += uppercase_weight

    # Lowercase letter check
    if re.search(r'[a-z]', password):
        score += lowercase_weight

    # Digit check
    if re.search(r'[0-9]', password):
        score += digit_weight

    # Special character check
    if re.search(r'[!@#$%^&*()_+{}":;<>,.?~`-]', password):
        score += special_char_weight

    # Username similarity check
    username_similarity = len(set(username.lower()).intersection(password.lower()))
    score += username_similarity_weight * username_similarity

    return max(0, score)

def main():
    
    input_flag = True
    
    while input_flag:
        username = input("Enter your username: ")
        password = input("Enter a password: ")
        
        password_strength = calculate_password_strength(username, password)

        if password_strength >= 8:
            print("Strong password! Good job.")
            input_flag =  False
        elif 4 <= password_strength < 8:
            print("Moderate password. Consider making it stronger.")
        else:
            print("Weak password. Please make it stronger.")


main()
