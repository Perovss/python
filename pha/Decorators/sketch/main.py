def foo():
    print('Вызвано foo')
    return 

# x = foo

# x()

# my_list = []

# my_list.append(foo)


# print(my_list)

# my_list[0]()

def mega_function(some_function):
    def new_function():
        print(f'Сейчас будет вызвана функция {some_function.__name__}')
        result = some_function()
        print(f'{some_function.__name__} вернула {result}')
        return result
    return new_function

mega_function(foo)()
