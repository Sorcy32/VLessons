"""
Домашнее задание №2
Работа csv
* Создайте список словарей с ключами name, age и job
* Запишите содержимое списка словарей в файл в формате csv
"""
import csv

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    db=[{"age":"18","job":"Курьер"},
        {"age":"25","job":"Дизайнер"},
        {"age":"66","job":"Пенсионер"},
        {"age":"30","job":"Строитель"},
        {"age":"29","job":"Писатель"}]
    filename='D_T_CSV.csv'
    try:
        with open(filename, 'w', newline= '', encoding='utf-8') as file:
            fieldnames=['age','job']
            writer=csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for row in db:
                writer.writerow(row)
            print("Успешно сохранено в файл:", filename)
    except:
        print("Ошибка при работе с файлом")
    
        



    
if __name__ == "__main__":
    main()
