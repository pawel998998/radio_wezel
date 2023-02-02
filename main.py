from config_setup import *
from datetime import datetime
import time

data = read_data("config.cfg")

numery_godzin = list(data.keys())

lista = []
lista2 = []
lista3 = []

for i in range(len(numery_godzin)):
	lista.append(data[numery_godzin[i]].split("-"))

for i in range(len(lista)):
	for x in range(2):
		lista2.append(lista[i][x])

for i in range(len(lista2)):
	godzina = lista2[i].split(":")
	for i in range(len(godzina)):
		godzina2 = int(godzina[0])
		minuta = int(godzina[1])
		czas = (godzina2*60)+(minuta)
		lista3.append(czas)

lista3 = list(dict.fromkeys(lista3))

def czas():
	dt = str(datetime.now())
	dt = dt.split(" ")
	dt = dt[1].split(":")
	godzina3 = int(dt[0])*60
	minuta3 = int(dt[1])
	czas2 = godzina3+minuta3
	return czas2



while True:
	time.sleep(5)
	czas3 = czas()
	#1
	if czas3 > 0 and czas3 < lista3[0]:
		set_vol_0()

	






