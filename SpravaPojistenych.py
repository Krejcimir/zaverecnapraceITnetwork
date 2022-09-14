class SpravaPojistenych:
    __seznamPojistenych = []

    def pridat(self, jmeno, příjmení, telefon, vek):
        self.__seznamPojistenych.append(Pojisteny(jmeno, příjmení, telefon, vek))

    def vypis(self):
        if not self.__seznamPojistenych:
            print("Záznam nenalezen.")
        for pojisteny in self.__seznamPojistenych:
            pojisteny.zobrazit()

    def smazat_vse(self):
        self.__seznamPojistenych = []

    def smazat(self, jmeno, příjmení, telefon, vek):
        for pojisteny in self.__seznamPojistenych:
            if pojisteny.jmeno == jmeno and pojisteny.příjmení == příjmení and pojisteny.telefon == telefon and pojisteny.vek == vek:
                self.__seznamPojistenych.remove(pojisteny)
                return True
        return False

    def vyhledat(self, jmeno, příjmení, telefon, vek):
        for pojisteny in self.__seznamPojistenych:
            if jmeno in pojisteny.jmeno and příjmení in pojisteny.příjmení and telefon in pojisteny.telefon and vek in pojisteny.vek:
                pojisteny.zobrazit()


class Pojisteny:
    jmeno = None
    příjmení = None
    telefon = None
    vek = None

    def __init__(self, jmeno, příjmení, telefon, vek):
        self.jmeno = jmeno
        self.příjmení = příjmení
        self.telefon = telefon
        self.vek = vek

    def zobrazit(self):
        print("""
            Jméno: %s,
            Příjmení: %s,
            Telefon: %s,
            Věk: %s""" % (self.jmeno, self.příjmení, self.telefon, self.vek))