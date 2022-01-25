
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




