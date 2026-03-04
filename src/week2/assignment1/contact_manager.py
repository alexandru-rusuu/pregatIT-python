contacts: list[dict] = []

def display_contact_details(contact: dict):
    print("=" * 20)
    for key, value in contact.items():
        print(f"{key}: {value}")
    print("=" * 20)

def add_contact(name: str, phone: str, **kwargs):
    new_contact: dict = {'name': name, 'phone': phone}
    new_contact.update(kwargs)
    contacts.append(new_contact)
    print(f"Contact {name} was added successfully. \n")

def display_all_contacts(sort_key: str = 'name', reverse: bool = False):
    if (len(contacts) == 0):
        print("Contact list is empty. \n")
        return

    sorted_contacts: list[dict] = sorted(contacts, key=lambda k: k.get(sort_key, ''), reverse=reverse)
    print(f"=== Contact list sorted by {sort_key} === \n")
    for c in sorted_contacts:
        display_contact_details(c)
    print("=" * 20)

def search_contacts(*args, **kwargs):
    results: list[dict] = []
    if args:
        for term in args:
            for c in contacts:
                if c['name'].startswith(term) or c['phone'].startswith(term):
                    if c not in results:
                        results.append(c)

    if kwargs:
        for key, value in kwargs.items():
            for c in contacts:
                if c.get(key) == value:
                    if c not in results: results.append(c)

    print("==== Search results ===")
    if not results:
        print("No results found. \n")
    for r in results:
        display_contact_details(r)

if __name__ == "__main__":
    pass