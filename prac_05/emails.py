emails_to_name = {}
user_email = input("Email: ").lower()

while user_email != '':
    if user_email in emails_to_name.keys():
        print("Email already in use")
        user_email = input("Email: ").lower()
    else:
        username = user_email.split('@')
        name = ' '.join(map(str, username[0].split('.'))).title()


        print(f"Is your name: {name}?")
        break

print(emails_to_name)
