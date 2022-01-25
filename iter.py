

class Iterr(list):
    def __iter__(self):
        return self

    def __next__(self):
        for i in self:
            return i

listt = Iterr([
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
])


for i in listt:
    print(i)



print(*(' '.join(m) for m in members), sep="\n")



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

