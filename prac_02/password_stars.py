def main():
    password = get_password()
    hide_password(password)


def hide_password(password):
    for i in range(len(password)):
        print("*", end="")


def get_password():
    min_length = 5
    password = input("Password: ")
    while len(password) < min_length:
        print("Invalid Password")
        password = input("Password: ")
    return password


main()