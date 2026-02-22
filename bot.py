def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter your command: ")
        command, *args = parse_input(user_input)

        if command in ["exit", "close"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter user name."

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    return f"Contact updated. New tel. number for {name} - {phone}"


@input_error
def show_phone(args, contacts):
    name = args[0]
    phone = contacts[name]
    return f"Phone number for contact {name} is {phone}"


def show_all(contacts):
    if not contacts:
        print("No contacts found.")

    result = ""

    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()


if __name__ == "__main__":
    main()

    