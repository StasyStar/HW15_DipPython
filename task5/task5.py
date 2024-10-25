"""
Задача 5. Запуск из командной строки
Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple. Каждый объект хранит: имя файла без расширения или название
каталога, расширение, если это файл, флаг каталога, название родительского каталога. В процессе сбора сохраните
данные в текстовый файл используя логирование.
"""

import logging
from collections import namedtuple
from pathlib import Path
import argparse

logging.basicConfig(filename='task5.log', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)
Files = namedtuple('File', 'name, extension, dir, parent')


def read_dir(path: str):
    path = Path(path)
    if not path.exists() or not path.is_dir():
        logger.error(f'Path does not exist or is not a directory: {path}')
        return
    for file in path.rglob('*'):
        obj = Files(file.stem if file.is_file() else file.name, file.suffix, file.is_dir(), file.parent)
        print(obj)
        logger.info(obj)


def walker():
    user_walker = argparse.ArgumentParser(
        description='user_walker',
        prog='read_dir()'
    )
    user_walker.add_argument('-p', '--path', help='Enter the path to the file')
    args = user_walker.parse_args()
    return read_dir(args.path)


if __name__ == '__main__':
    walker()

    # Примеры вызовов:
    # python3 task5.py -p ../../seminar15_standart_packages
    # python3 task5.py -p /Users/stasy/Documents/Education/GB/Python/dip/seminars/seminar15_standart_packages
