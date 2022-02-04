listt = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator:

    def __init__(self, some_list):
        self.main_list = some_list
        self.lenn = len(some_list)

    def __iter__(self):
        self.main_list_cursor = 0
        self.nested_list_cursor = -1
        return self

    def __next__(self):

        self.nested_list_cursor += 1
        if self.nested_list_cursor == len(self.main_list[self.main_list_cursor]):
            self.main_list_cursor += 1
            self.nested_list_cursor = 0

        if self.main_list_cursor == len(self.main_list):
            raise StopIteration
        return self.main_list[self.main_list_cursor][self.nested_list_cursor]


for item in FlatIterator(listt):
    print(item)

flat_list = [item for item in FlatIterator(listt)]

print(flat_list)

