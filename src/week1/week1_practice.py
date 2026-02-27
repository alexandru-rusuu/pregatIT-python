from datetime import datetime

data_Nastere: str = input("Data nastere: DD/MM/YYYY: ")
nume: str = input("Nume: ")
tara: str = input("Tara: ")

parti: list[str] = data_Nastere.replace('.','/').split('/')


este_format_valid: bool = len(parti) == 3 and all([p.isdigit() for p in parti])

if(not este_format_valid):
    print("Data nastere trebuie sa fie valida! (DD/MM/YYYY)\n")
else:
    zi, luna, an = [int(p) for p in parti]
    if(not (1 <= luna <= 12) or not (1<= zi <= 31) or an < 1900):
        print("Data nastere trebuie sa fie valida! (Ziua 1-31), Luna(1-12), An(>1900).\n")
    else:
        an_Curent: int = datetime.now().year
        varsta: int = an_Curent - an;
        varsta_Major: int = 18

        mesaje_Output: list[str] = [
            f"* Bravo, {nume}, legal ai voie sa {actiune} in {tara}!\n"
            for actiune, limita in [("votezi", varsta_Major), ("conduci", varsta_Major)]
            if varsta >= limita
        ]

        if mesaje_Output:
            [print(mesaj) for mesaj in mesaje_Output]
        else:
            print(f"Din pacate, {nume}, esti prea tanar!")

if __name__ == '__main__':
    pass