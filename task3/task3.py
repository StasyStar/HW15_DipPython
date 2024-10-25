"""
Задача 3. Планирование задач
Напишите функцию, которая принимает количество дней от текущей даты и возвращает дату, которая наступит через
указанное количество дней. Дополнительно, выведите эту дату в формате YYYY-MM-DD.
"""

from datetime import datetime, timedelta


def future_date(days_num):
    today = datetime.now()
    time_delta = timedelta(days=days_num)
    res_date = today + time_delta
    print(res_date.strftime(f'In {days_num} it will be: %Y-%m-%d'))


if __name__ == '__main__':
    future_date(6)
