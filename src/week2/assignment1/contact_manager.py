contacte = []

def afiseaza_Detalii_Contact(contact: dict):
    print("=" * 20)
    for key, value in contact.items():
        print(f"{key}: {value}")
    print("=" * 20)

def adauga_Contact(nume: str, telefon: str, **kwargs):
    contact_Nou = {'nume': nume, 'telefon': telefon}
    contact_Nou.update(kwargs)
    contacte.append(contact_Nou)
    print(f"Contactul {nume} a fost adaugat cu succes. \n")

def afiseaza_Toate_Contactele(sort_key: str = 'nume',reverse: bool = False):
    if (len(contacte) == 0):
        print("Lista de contacte e goala. \n");
        return

    contacte_Sortate = sorted(contacte, key=lambda k: k.get(sort_key, ''), reverse=reverse)
    print(f"=== Lista contacte sortate dupa {sort_key} === \n")
    for c in contacte_Sortate:
        afiseaza_Detalii_Contact(c)
    print("=" * 20)

def cauta_Contacte(*args, **kwargs):
    rezultate = []
    if args:
        for term in args:
            for c in contacte:
                if c['nume'].startswith(term) or c['telefon'].startswith(term):
                    if c not in rezultate:
                        rezultate.append(c)

    if kwargs:
        for key, value in kwargs.items():
            for c in contacte:
                if c.get(key) == value:
                    if c not in rezultate: rezultate.append(c)

    print("==== Rezultate cautare ===")
    if not rezultate:
        print("Nu s au gasit rezultate. \n");
    for r in rezultate:
        afiseaza_Detalii_Contact(r)

