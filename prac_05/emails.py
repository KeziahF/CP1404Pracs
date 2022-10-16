"""
CP1404 Prac
Emails
Estimate: 30 minutes
Actual: 45 minutes
"""
def main(user_email):
    email_to_name = {}
    user_email = input("Email: ").lower()
    while user_email != '':
        if user_email in email_to_name.keys():
            print("Email already in use")
            user_email = input("Email: ").lower()
        else:
            extract_name(user_email, email_to_name)

        user_email = input("Email: ").lower()

    for pair in email_to_name.items():
        print(f"{pair[1]}  ({pair[0]})")
def extract_name(user_email, email_to_name):
    yes_choice = ['yes', 'y']
    no_choice = ['no', 'n']
    username = user_email.split('@')
    name = ' '.join(map(str, username[0].split('.'))).title()
    correct_name = input(f"Is your name: {name}? (y/n) ").lower()
    if correct_name in no_choice:
        name = input("Name: ").lower().title()
    email_to_name[user_email] = name
    return email_to_name


user_email = 'email'
main(user_email)
