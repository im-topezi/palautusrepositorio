from kps import KiviPaperiSakset
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KiviPaperiSakset):
    def _toisen_siirto(self,ensimmainen_siirto):
        tekoaly = TekoalyParannettu(10)
        ekan_siirto = ensimmainen_siirto
        tokan_siirto = tekoaly.anna_siirto()
        tekoaly.aseta_siirto(ekan_siirto)
        print(f"Tietokone valitsi: {tokan_siirto}")
        return tokan_siirto
