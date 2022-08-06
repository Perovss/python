from functools import wraps

def cached(max_sise):   
    def _cached(old_function):
        CACHE = {}

        @wraps(old_function)
        def new_function(*args, **kwargs):
            key = f'{args}{kwargs}'
            print(key)
            if key in CACHE:
                return CACHE[key]

            result = old_function(*args, **kwargs)
            CACHE[key] = result
            if len(CACHE) >= max_sise:
                CACHE.popitem()

            return result

        return new_function
    return _cached
