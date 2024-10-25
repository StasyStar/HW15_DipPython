"""
Задание 1. Логирование с использованием нескольких файлов
Напишите скрипт, который логирует разные типы сообщений в разные файлы.
Логи уровня DEBUG и INFO должны сохраняться в debug_info.log, а логи уровня WARNING и выше — в warnings_errors.log.
"""

import logging


class TestFunction:
    def __init__(self, num, logger):
        self.my_logger = logger
        if isinstance(num, int):
            if num >= 0:
                self.num = num
            else:
                self.my_logger.log.warning(f'User try to input negative number: {num}')
                raise ValueError('Please use the positive number')
        else:
            self.my_logger.log.error(f'User try to input text: {num}')
            raise TypeError(f'Please use integer, not the {type(num)}')

    def factorial(self):
        res = 1
        for i in range(1, self.num + 1):
            res *= i
            self.my_logger.log.debug(f'In iteration {i}: {res // i} x {i} = {res}')
        self.my_logger.log.info(f'Factorial of {self.num} is {res}')
        return res


class MyLogger:
    def __init__(self):
        self.log = None

    def log_file(self):
        self.log = logging.getLogger(__name__)
        self.log.setLevel(logging.DEBUG)
        formatter = logging.Formatter('{asctime}:{levelname}:{message}', style='{')

        debug_handler = logging.FileHandler('debug_info.log', mode='w', encoding='utf-8')
        debug_handler.setLevel(logging.DEBUG)
        debug_handler.setFormatter(formatter)
        self.log.addHandler(debug_handler)

        error_handler = logging.FileHandler('warnings_errors.log', mode='w', encoding='utf-8')
        error_handler.setLevel(logging.WARNING)
        error_handler.setFormatter(formatter)
        self.log.addHandler(error_handler)


if __name__ == '__main__':
    my_logger = MyLogger()
    my_logger.log_file()

    try:
        test1 = TestFunction(5, my_logger)
        print(test1.factorial())
        test2 = TestFunction(-1, my_logger)  # Это вызовет ошибку
    except ValueError as e:
        print(e)
    try:
        test3 = TestFunction("smth interesting", my_logger)  # Это вызовет ошибку
    except TypeError as e:
        print(e)
