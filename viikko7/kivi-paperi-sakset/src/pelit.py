from kps_parempi_tekoaly import KPSParempiTekoaly
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly

def luo_peli(peli):
    if peli=="a":
        return KPSPelaajaVsPelaaja()
    elif peli=="b":
        return KPSTekoaly()
    elif peli=="c":
        return KPSParempiTekoaly()
    else:
        return None