def is_valid_password(password):
    return len(password) >= 8
def slugify(text):
    return text.lower().replace(" ", "-")