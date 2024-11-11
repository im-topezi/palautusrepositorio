#tehdään importit

from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan")

x = int(input("luku 1: "))
y = int(input("luku 2: "))
print(f"{summa(x, y)}") #muutoksia
print(f"{erotus(x, y)}") #muutoksia

logger("lopetetaan")

#lisäys
