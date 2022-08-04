from itertools import chain
nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

class FlatIterator(list):
    def __iter__(self):
        values = chain.from_iterable(nested_list)
        return values

print(f'\n{"-" * 10} Итераторы {"-" * 10}')
for item in FlatIterator(nested_list):
	print(item)
print(f'\n')
flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)


def flat_generator(nested_list):
    for sub in nested_list:
        for element in sub:
            yield element

flat_generator_list = [item for item in flat_generator(nested_list)]
print(f'\n{"-" * 10} Генераторы {"-" * 10}')
print(flat_generator_list)
print(f'\n')
for num in flat_generator(nested_list):
    print(num)

