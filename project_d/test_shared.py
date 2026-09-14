import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from shared_package import is_valid_password, slugify

password = "hello"
text = "Python Package Reuse"

print("Project D")
print("Password valid:", is_valid_password(password))
print("Slug:", slugify(text))