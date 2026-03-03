from contact_manager import add_contact, display_all_contacts, search_contacts

if __name__ == "__main__":
    add_contact("Raul", "0785642312", email="raul@gmail.com")
    add_contact("Andreea", "0783423412", email="andreea@email.com")

    while True:
        print("=== Contact Manager ===")
        print("1. Add contact")
        print("2. Display contacts")
        print("3. Search contact")
        print("4. Exit")

        choice: str = input("Choose an option: ")

        if choice == "1":
            name: str = input("Name: ")
            phone: str = input("Phone: ")
            email: str = input("Email (optional): ")
            if email:
                add_contact(name, phone, email=email)
            else:
                add_contact(name, phone)

        elif choice == "2":
            display_all_contacts()

        elif choice == "3":
            term: str = input("Enter the start of the name or phone to search: ")
            search_contacts(term)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("=== Invalid option ===")