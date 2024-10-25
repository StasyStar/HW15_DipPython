"""
Задача 2. Работа с текущим временем и датой
Напишите скрипт, который получает текущее время и дату, а затем выводит их в формате YYYY-MM-DD HH:MM:SS.
Дополнительно, выведите день недели и номер недели в году
"""

from datetime import datetime


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


if __name__ == '__main__':
    get_date()


