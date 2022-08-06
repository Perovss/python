def make_trace(some_function):
    def new_function(*args,**kwargs):
        print(f'Сейчас будет вызвана функция {some_function.__name__}')
        print(f'с аргументами {args} и {kwargs}')
        result = some_function(*args,**kwargs)
        print(f'{some_function.__name__} вернула {result}')
        return result
    return new_function
