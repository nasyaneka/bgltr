nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]


def flat_generator(listt):
	for lists in listt:
		cnt1 = 0
		while cnt1 < len(listt):
			yield lists[cnt1]
			cnt1 += 1


for item in flat_generator(nested_list):
	print(item)
