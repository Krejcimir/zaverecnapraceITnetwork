import SpravaPojistenych


class KonzoleZadani:
    SpravaPojistenych = None

    def __init__(self):
        self.SpravaPojistenych = SpravaPojistenych.SpravaPojistenych()

    def __info_od_uzivatele(self):
        print("Prosím zadejte jméno pojištěného")
        jmeno = input()
        print("Prosím zadajte příjmení pojištěného")
        prijmeni = input()
        print("Prosím zadejte telefonní číslo pojištěného")
        telefon = input()
        print("Prosím zadejte věk pojištěného")
        vek = input()
        return (jmeno, prijmeni, telefon, vek)

    def __pridat_do_vypisu(self):
        jmeno, prijmeni, telefon, vek = self.__info_od_uzivatele()
        self.SpravaPojistenych.pridat(jmeno, prijmeni, telefon, vek)

    def __smazat_z_vypisu(self):
        jmeno, prijmeni, telefon, vek = self.__info_od_uzivatele()
        if self.SpravaPojistenych.smazat(
                jmeno, prijmeni, telefon, vek):
            print("Záznam smazán!")
        else:
            print("Záznam nenalazen, zadejte znovu.")

    def __vytvorit_hledani(self):
        hotovo = False
        jmeno = ""
        prijmeni = ""
        telefon = ""
        vek = ""

        while not hotovo:
            print("""Jaké informace chcete vyhledat?
                Jméno
                Příjmení
                Telefon
                Věk?""")
            odpoved = input()
            if odpoved.lower() == "jmeno":
                print("Zadejte jméno:")
                jmeno = input()
            else:
                if odpoved.lower() == "prijmeni":
                    print("Zadejte příjmení:")
                    prijmeni = input()
                else:
                    if odpoved.lower() == "telefon":
                        print("Zadejte telefonní číslo:")
                        telefon = input()
                    else:
                        if odpoved.lower() == "vek":
                            print("Zadejte věk:")
                            vek = input()
                        else:
                            print("Prosím zadejte správné údaje")
            print("Chcete přidat další informace? (y/n)")
            hotovo = input() == "n"
        self.SpravaPojistenych.vyhledat(jmeno, prijmeni, telefon, vek)

    def __operace(self, odpoved):
        if odpoved.lower() == "výpis":
            self.SpravaPojistenych.vypis()
            return True
        if odpoved.lower() == "přidat":
            self.__pridat_do_vypisu()
            return True
        if odpoved.lower() == "smazat":
            self.__smazat_z_vypisu()
            return True
        if odpoved.lower() == "smazat_vše":
            self.SpravaPojistenych.smazat_vse()
            print("Všechny kontakty smazány")
            return True
        if odpoved.lower() == "vyhledat":
            self.__vytvorit_hledani()
            return True
        if odpoved.lower() == "zavřít":
            print("Nashledanou")
            return False
        else:
            print("Špatné zadání, prosím zvolte správné zadání")
            return True

    def spustit(self):
        spusteno = True
        uvitat = "Vítejte v evidenci pojištěných\n"
        menu = """Zvolte akci\n
        | Výpis      | - Vypsat všechny pojištěné
        | Přidat     | - Přidat nového pojistného
        | Smazat     | - Smaže pojišteného
        | Smazat_vše | - Smaže všechny pojištěné
        | Vyhledat   | - Vyhledá uživatele
        | Zavřít     | - Zavře adresář"""
        print(uvitat)
        while spusteno:
            print(menu)
            odpoved = input()
            spusteno = self.__operace(odpoved)
