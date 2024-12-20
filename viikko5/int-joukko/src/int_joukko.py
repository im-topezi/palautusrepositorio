


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        for i in range(self.alkioiden_lkm):
            if n == self.ljono[i]:
                return True
        return False

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm +=  1
            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm % len(self.ljono) == 0:
                taulukko_old = self.ljono
                self.ljono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_lista(taulukko_old, self.ljono)

            return True
        return False

    def poista(self, n):
        listan_kohta = None

        for i in range(self.alkioiden_lkm):
            if n == self.ljono[i]:
                listan_kohta = i  # siis luku löytyy tuosta kohdasta :D
                self.ljono[listan_kohta] = 0
                break

        if isinstance(listan_kohta,int):
            for j in range(listan_kohta, self.alkioiden_lkm - 1):
                self.ljono[j],self.ljono[j + 1]=self.ljono[j + 1],self.ljono[j]
            self.alkioiden_lkm -= 1
            return True

        return False

    def kopioi_lista(self, lista_a, lista_b):
        for i in range(len(lista_a)):
            lista_b[i] = lista_a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)
        for i in range(len(taulu)):
            taulu[i] = self.ljono[i]
        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        for i in range(len(a_taulu)):
            x.lisaa(a_taulu[i])
        for i in range(len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        for i in range(len(a_taulu)):
            for j in range(len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        for i in range(len(a_taulu)):
            z.lisaa(a_taulu[i])
        for i in range(len(b_taulu)):
            z.poista(b_taulu[i])
        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        else:
            tuotos = "{"
            for i in range(self.alkioiden_lkm - 1):
                tuotos += str(self.ljono[i])+ ", "
            tuotos += str(self.ljono[self.alkioiden_lkm - 1]) + "}"
            return tuotos
