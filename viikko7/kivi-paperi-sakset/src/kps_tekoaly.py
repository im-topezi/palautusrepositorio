from kps import KiviPaperiSakset
from tekoaly import Tekoaly


class KPSTekoaly(KiviPaperiSakset):
    def _toisen_siirto(self,ensimmainen_siirto):
        tekoaly= Tekoaly()
        tokan_siirto = tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        return tokan_siirto

