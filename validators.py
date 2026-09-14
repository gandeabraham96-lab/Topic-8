def validate_age(age):
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120")

    return True