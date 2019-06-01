"""
Домашнее задание №2
Дата и время
* Напечатайте в консоль даты: вчера, сегодня, месяц назад
* Превратите строку "01/01/17 12:10:03.234567" в объект datetime
"""
from datetime import datetime, timedelta


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    dt=datetime.now()
    print('Вчера      : ', datetime.strftime(dt+timedelta(days=-1), "%d.%m.%Y"))
    print('Сегодня    : ', datetime.strftime(dt, "%d.%m.%Y"))
    print('Месяц назад: ', datetime.strftime(dt.replace(month=(dt.month-1)), "%d.%m.%Y"))

    
    
def str_2_datetime(string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    dt=datetime.strptime(string, "%d/%m/%y %X.%f")
    return dt

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/17 12:10:03.234567"))
