import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from shared_package import is_valid_password, slugify

password = "python123"
text = "Advanced Python Topics"

print("Project C")
print("Password valid:", is_valid_password(password))
print("Slug:", slugify(text))