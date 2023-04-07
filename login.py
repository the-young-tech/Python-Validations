# run python3 login.py ->> no modules are need to run this
# you can change the username and password

def login(user, passwd):
    if user == "Admin":
        if passwd == "passwd":
            return user
        else:
            raise ValueError("\033[91mIncorrect Password\033[0m")
    else:
        raise ValueError("\033[91mIncorrect Username\033[0m")

try:
    user = input("Enter the username: ")
    passwd = input("Enter the password: ")
    result = login(user, passwd)
    print("\033[92mWelcome Back", result, "\033[0m")
except ValueError as err:
    print(err)
