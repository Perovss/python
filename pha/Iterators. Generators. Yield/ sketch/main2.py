from itertools import chain
my_dict = {'a':'1', 'b':{'c':'2'}}

# for item in my_dict.values():
#     print(item)

class My_dict(dict):

    def __iter__(self):
        self._values = iter(self.values())
        return self
    

    def __next__(self):
        next_value = next(self._values)
        if isinstance(next_value, dict):
            self._values = chain(self._values, next_value.values())
            return next(self._values)
        return next_value


for item in My_dict({'a':'1', 'b':{'c':'2'}}):
    print(item)