import logging

Log_Format = "%(levelname)s %(asctime)s - %(message)s"

def logger():
    def _decorator(_function):
        def _tracer(*args, **kwargs):
            logging.basicConfig(filename = "logs/results.log",
                filemode = "a",
                format = Log_Format, 
                level = logging.INFO,
                datefmt='%m/%d/%Y %H:%M')
            logger = logging.getLogger()
            logger.info(f'вызвана функция {_function.__name__} c аргументами: {args} {kwargs}.')
            result = _function(*args, **kwargs)
            logger.info(f'Результат выполнения функции: \n{result}')
            return result
        return _tracer
    return _decorator
