num_numbers = 5
values = []
menu = 'Number checker (n) or usernames (u)?: '
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

def number_checker():
    try:
        for i in range(num_numbers):
            values.append(int(input('Number: ')))
    except ValueError:
        print('Invalid input')

    print('The first number is %s' % (values[0]))
    print('The last number is %s' % (values[-1]))
    print('The smallest number is %s' % (min(values)))
    print('The largest number is %s' % (max(values)))
    print('The average of the numbers is %s' % (sum(values) / 2))

def username_entry():
    username = input('What is your username?: ')
    if username in usernames:
        print('Access Granted')
    else:
        print('Access Denied')

def main():
    user_input = False
    choice = input(menu).lower()
    while user_input == False:
        if choice == 'u':
            username_entry()
            user_input = True
        elif choice == 'n':
            number_checker()
            user_input = True
        else:
            print('invalid entry')
            choice = input(menu).lower()
            user_input = False



main()