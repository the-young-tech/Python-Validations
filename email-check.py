# It requires the module re to run the file.
# Run -> python3 email-check.py to see if a email is valid.

import re

GREEN = "\033[92m"
RED = "\033[91m"
END_COLOR = "\033[0m"

def is_valid(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

custom = str(input())
if is_valid(custom):
    print(custom + " -> " + GREEN + "This is a valid email address." + END_COLOR)
else:
    print(custom + " -> " + RED + "This is not a valid email address." + END_COLOR)
