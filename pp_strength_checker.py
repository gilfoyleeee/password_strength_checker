import re

def check_password_strength(password):
    """Evaluate the strength of a password."""
    strength = "Weak"
    score = 0

    # Criteria for scoring
    if len(password) >= 8:
        score += 1
    if re.search(r'[A-Z]', password):  # Contains uppercase letter
        score += 1
    if re.search(r'[a-z]', password):  # Contains lowercase letter
        score += 1
    if re.search(r'[0-9]', password):  # Contains digit
        score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):  # Contains special character
        score += 1

    # Determine strength based on score
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength

if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    strength = check_password_strength(password)
    print(f"Password Strength: {strength}")
