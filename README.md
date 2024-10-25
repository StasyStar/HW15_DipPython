# Домашняя работа к семинару №15. Обзор стандартной библиотеки Python
## Задание №1
Логирование с использованием нескольких файлов
Напишите скрипт, который логирует разные типы сообщений в разные файлы.
Логи уровня DEBUG и INFO должны сохраняться в debug_info.log, а логи уровня WARNING и выше — в warnings_errors.log.

### Класс TestFunction
Инициализирован класс с тестовой функцией расчета факториала с перехватом ошибок
```
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
```
### Класс MyLogger
Инициализирован класс для логирования ошибок в зависимости от их уровня в два файла: debug_info.log, warnings_errors.log
```
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
```
## Задание №2
Работа с текущим временем и датой
Напишите скрипт, который получает текущее время и дату, а затем выводит их в формате YYYY-MM-DD HH:MM:SS.
Дополнительно, выведите день недели и номер недели в году

### Функция get_date()
Создана функция для преобразования текущих даты и времени в нужный формат, а так же вывод дня недели и ее номер с 
начала года.
```
def get_date():
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    hour = datetime.now().hour
    minute = datetime.now().minute
    second = datetime.now().second
    dt = datetime(year, month, day, hour, minute, second)
    print(dt)
    print(dt.strftime(f'Today is %A and it is %W week from the beginning of the {year} year'))
```
## Задание №3
Планирование задач
Напишите функцию, которая принимает количество дней от текущей даты и возвращает дату, которая наступит через
указанное количество дней. Дополнительно, выведите эту дату в формате YYYY-MM-DD.

### Функция future_date()
Создана функция для вывода будующей даты в соответствующем формате с помощью прибавления к текущей заданного количества 
дней.
```
def future_date(days_num):
    today = datetime.now()
    time_delta = timedelta(days=days_num)
    res_date = today + time_delta
    print(res_date.strftime(f'In {days_num} it will be: %Y-%m-%d'))
```

## Задание №4
Опции и флаги
Напишите скрипт, который принимает два аргумента командной строки: число и строку. Добавьте следующие опции:
- --verbose, если этот флаг установлен, скрипт должен выводить дополнительную информацию о процессе.
- --repeat, если этот параметр установлен, он должен указывать, сколько раз повторить строку в выводе.

### Функция parse()
Создана функция для получения аргументов от пользователя через командную строку и преобразование их к нужному 
формату для функции print_phrase()
```
def parse():
    user_parser = argparse.ArgumentParser(
        description='user_parser',
        epilog='If we do not have the parameters program return 1st week in month',
        prog='print_phrase()'
    )
    user_parser.add_argument('-v', '--verbose', help='Enter "true" if you need information', default=False)
    user_parser.add_argument('-r', '--repeat', help='Enter a number of repetitions of the phrase', default=1)
    args = user_parser.parse_args()
    verbose = args.verbose.lower()
    repeat = int(args.repeat)
    return print_phrase(verbose, repeat)
```
### Функция print_phrase()
Функция для вывода фразы repeat-раз.
```
def print_phrase(verbose, repeat):
    if verbose:
        print('Some helpfully information\n' * repeat)
    else:
        print('No verbose output.')
```
## Задание №5
Запуск из командной строки
Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple. Каждый объект хранит: имя файла без расширения или название
каталога, расширение, если это файл, флаг каталога, название родительского каталога. В процессе сбора сохраните
данные в текстовый файл используя логирование.

### Функция read_dir()
Создана функция для обхода соответствующей директории и вывода информации об имени файла, его расширении, флаге 
каталога, названии родительского каталога.
```
def read_dir(path: str):
    path = Path(path)
    if not path.exists() or not path.is_dir():
        logger.error(f'Path does not exist or is not a directory: {path}')
        return
    for file in path.rglob('*'):
        obj = Files(file.stem if file.is_file() else file.name, file.suffix, file.is_dir(), file.parent)
        print(obj)
        logger.info(obj)
```
### Функция walker()
Создана функция для получения аргументов от пользователя через командную строку и преобразование их к нужному 
формату для функции read_dir()
```
def walker():
    user_walker = argparse.ArgumentParser(
        description='user_walker',
        prog='read_dir()'
    )
    user_walker.add_argument('-p', '--path', help='Enter the path to the file')
    args = user_walker.parse_args()
    return read_dir(args.path)
```