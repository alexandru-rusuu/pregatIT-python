from asyncio import wait

from contact_manager import adauga_Contact, afiseaza_Toate_Contactele, cauta_Contacte

def exemplu_Meniu():
    adauga_Contact("Raul", "0785642312", email="raul@gmail.com")
    adauga_Contact("Andreea", "0783423412", email="andreea@email.com")

    while True:
        print("=== Manger de Contacte ===")
        print("1. Adauga contact ")
        print("2. Afiseaza contacte ")
        print("3. Cauta contact ")
        print("4. Exit ")

        optiune = input("Alege o optiune: ")
        if optiune == "1":
            nume = input("Nume: ")
            telefon = input("Telefon: ")
            email = input("Email (optional): ")
            if email:
                adauga_Contact(nume, telefon, email=email)
            else:
                adauga_Contact(nume, telefon)

        elif optiune == "2":
            afiseaza_Toate_Contactele()

        elif optiune == "3":
            termen = input("Introdu inceputul numelui sau telefonului pt. cautare: ")
            cauta_Contacte(termen)

        elif optiune == "4":
            print("Iesire")
            break

        else:
            print("=== Optiune invalida ===")

if __name__ == "__main__":
        exemplu_Meniu()
