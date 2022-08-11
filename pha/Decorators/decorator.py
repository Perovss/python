import logging

Log_Format = "%(levelname)s %(asctime)s - %(message)s"

def logger(log_file_name):
    def _decorator(_function):
        def _tracer(*args, **kwargs):
            logging.basicConfig(filename = log_file_name,
                filemode = "a",
                format = Log_Format, 
                level = logging.INFO,
                datefmt='%m/%d/%Y %H:%M')
            logger = logging.getLogger()
            logger.info(f'вызвана функция {_function.__name__} c аргументами: {args} {kwargs}.')
            result = _function(*args, **kwargs)
            logger.info(f'Результат выполнения функции: \n{result}')
            logger.warning(f'Результат сохранен в {log_file_name}')
            return result   
        return _tracer
    return _decorator
