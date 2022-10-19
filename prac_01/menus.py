MENU_STRING = "(H)ello\n(G)oodbye\n(Q)uit"
name = str(input("Enter name: "))
print(MENU_STRING)
choice = str(input(""))
while choice != "Q":
    if choice == "H":
        print(F"Hello {name}")
    elif choice == "G":
        print(F"Goodbye {name}")
    else:
        print("Invalid Message")
    print(MENU_STRING)
    choice = str(input(""))
print("Finished")
