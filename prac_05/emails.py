"""
CP1404 Practical
Emails
Emails to name dictionary
Estimate: 30 minutes
Actual: 45 minutes
"""


def main():
    """Takes user email input, collects name and displays dictionary results"""
    email = input("Email: ").lower()
    collect_email(email)


def collect_email(email):
    """Collects email input and displays resultant dictionary"""
    email_to_name = {}
    while email != '':
        if email in email_to_name.keys():
            print("Email already in use")
            email = input("Email: ").lower()
        else:
            extract_name(email, email_to_name)

        email = input("Email: ").lower()

    for pair in email_to_name.items():
        print(f"{pair[1]}  ({pair[0]})")


def extract_name(email, email_to_name):
    """Creates email_to_name dictionary"""
    yes_choice = ['yes', 'y']
    no_choice = ['no', 'n']
    username = email.split('@')
    name = ' '.join(map(str, username[0].split('.'))).title()
    confirmation = input(f"Is your name: {name}? (y/n) ").lower()
    if confirmation in no_choice:
        name = input("Name: ").lower().title()
    email_to_name[email] = name
    return email_to_name


main()
