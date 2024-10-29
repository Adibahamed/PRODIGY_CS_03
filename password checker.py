def check_password_strength(password):
    """
    Check password strength based on multiple criteria and provide feedback.
    Returns a tuple of (strength_score, list of feedback messages)
    """
    feedback = []
    score = 0
    
    # Check length
    if len(password) < 8:
        feedback.append("Password is too short. Minimum length is 8 characters.")
    elif len(password) >= 12:
        score += 2
        feedback.append("Good length!")
    else:
        score += 1
    
    # Check lowercase
    if not any(c.islower() for c in password):
        feedback.append("Add lowercase letters.")
    else:
        score += 1
        
    # Check uppercase
    if not any(c.isupper() for c in password):
        feedback.append("Add uppercase letters.")
    else:
        score += 1
        
    # Check numbers
    if not any(c.isdigit() for c in password):
        feedback.append("Add numbers.")
    else:
        score += 1
        
    # Check special characters
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if not any(c in special_chars for c in password):
        feedback.append("Add special characters.")
    else:
        score += 1
        
    # Determine strength based on score
    if score < 2:
        strength = "Very Weak"
    elif score < 3:
        strength = "Weak"
    elif score < 4:
        strength = "Moderate"
    elif score < 5:
        strength = "Strong"
    else:
        strength = "Very Strong"
        
    return strength, feedback

# Example usage function
def check_password():
    password = input("Enter your password: ")
    strength, feedback = check_password_strength(password)
    
    print(f"\nPassword Strength: {strength}")
    
    if feedback:
        print("\nImprovement suggestions:")
        for suggestion in feedback:
            print(f"- {suggestion}")
    else:
        print("\nExcellent! Your password meets all criteria.")

# Run the password checker
if __name__ == "__main__":
    check_password()