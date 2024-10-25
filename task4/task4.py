"""
Задача 4. Опции и флаги
Напишите скрипт, который принимает два аргумента командной строки: число и строку. Добавьте следующие опции:
● --verbose, если этот флаг установлен, скрипт должен выводить дополнительную информацию о процессе.
● --repeat, если этот параметр установлен, он должен указывать, сколько раз повторить строку в выводе.
"""

import argparse


def parse():
    user_parser = argparse.ArgumentParser(
        description='user_parser',
        epilog='If we do not have the parameters program return 1st week in month',
        prog='print_phrase()'
    )
    user_parser.add_argument('-v', '--verbose', help='Enter "true" if you need information', default=False)
    user_parser.add_argument('-r', '--repeat', help='Enter a number of repetitions of the phrase', default=1)
    args = user_parser.parse_args()
    verbose = args.verbose.lower() == 'true'
    repeat = int(args.repeat)
    return print_phrase(verbose, repeat)


def print_phrase(verbose, repeat):
    if verbose:
        print('Some helpfully information\n' * repeat)
    else:
        print('No verbose output.')


if __name__ == '__main__':
    print(parse())

    # Пример вызова:
    # python3 task4.py -v True -r 3


