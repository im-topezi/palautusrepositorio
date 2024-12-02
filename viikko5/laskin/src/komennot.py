class Summa:
    def __init__(self,sovelluslogiikka,syote):
        self.logiikka=sovelluslogiikka
        self.syote=syote
    def suorita(self):
        self.logiikka.plus(self.syote())

class Erotus:
    def __init__(self,sovelluslogiikka,syote):
        self.logiikka=sovelluslogiikka
        self.syote=syote
    def suorita(self):
        self.logiikka.miinus(self.syote())

class Nollaus:
    def __init__(self,sovelluslogiikka,syote):
        self.logiikka=sovelluslogiikka
        self.syote=syote
    def suorita(self):
        self.logiikka.nollaa()

class Kumoa:
    def __init__(self,sovelluslogiikka,syote):
        self.logiikka=sovelluslogiikka
    def suorita(self):
        self.logiikka.arvot.pop()
        self.logiikka.aseta_arvo(self.logiikka.arvot[-1])