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
    some_function()
    some_function()

mega_function(foo)