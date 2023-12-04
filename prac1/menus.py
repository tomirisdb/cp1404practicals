"""
get name
display MENU
get choice
while choice != Q
   if choice == H
       display "Hello" name
   else if choice == G
       display "Goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""
MENU = "(H)ello\n(G)oodbye\n(Q)uit"
name = input("Enter name: ")
print(MENU)
choice = input("").upper()
while choice != "Q":
    if choice == "H":
        print(f'Hello {name}')
    elif choice == "G":
        print(f'Goodbye {name}')
    else:
        print("Invalid choice")
    print(MENU)
    choice = input("").upper()
print("Finished.")

