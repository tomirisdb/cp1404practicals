"""
Pseudocode:
function main
    email_to_name = {}
    get email
    while email != ""
        name = get_name_from_email(email)
        get verification
        if verification.upper() != "Y" and verification != ""
            get name
        email_to_name[email] = name
        get email
    for email, name in email_to_name.items():
        display name, email

function get_name_from_email(email)
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = "".join(parts).title()
    return name
"""


def main():
    """Collects user emails, extracts names, and prints the results."""
    email_to_name = {}
    email = input("Enter your email: ")
    while email != "":
        name = get_name_from_email(email)
        verification = input(f'Is your name? {name} (Y/n)')
        if verification.upper() != "Y" and verification != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f'{name} ({email})')


def get_name_from_email(email):
    """Extracts a person's name from an email address."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = "".join(parts).title()
    return name


main()
