listt = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]

def Mygen(list):
	cont = 0
	cont1 = 0
	while list[cont] in list:
		cont2 = cont1
		while list[cont][cont2] in list[cont]:
			yield list[cont][cont2]
			cont2 += 1
			continue
		cont += 1
		continue

for i in Mygen(listt):
	print(i)

