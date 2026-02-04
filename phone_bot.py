from pathlib import Path
from colorama import Fore, init

init(autoreset=True)

separator = ", "

def get_saved_contacts(path = "data/contacts.txt"):
    contacts = {}
    try:
        with open(Path(path), "r") as file:
            for line in file:
                name, phone = line.strip().split(separator)
                contacts[name] = phone
    except FileNotFoundError:
        pass
    return contacts

def save_contacts(contacts, path = "data/contacts.txt"):
    with open(Path(path), "w") as file:
        for name, phone in contacts.items():
            file.write(f"{name}{separator}{phone}\n")
        print(Fore.GREEN + "Contacts saved successfully.")


def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        return "Contact does not exist."
    contacts[name] = phone
    return Fore.GREEN + "Contact updated."


def show_phone(args, contacts):
    name = args[0]
    if name not in contacts:
        return "Contact does not exist."
    return Fore.BLUE + contacts[name]


def print_all_contacts(contacts):
    for name, phone in contacts.items():
        print(f"{Fore.CYAN}{name}: {Fore.BLUE}{phone}")


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return "Contact already exists."
    contacts[name] = phone
    return "Contact added."

def main():
    print(Fore.GREEN + "Welcome to the assistant bot!")
    contacts = get_saved_contacts()

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            save_contacts(contacts)
            print(Fore.GREEN + "Good bye!")
            break
        elif command == "hello":
            print(Fore.GREEN + "How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print_all_contacts(contacts)
        else:
            print(Fore.RED + "Invalid command.")


if __name__ == "__main__":
    main()
    