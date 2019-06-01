"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
from functools import reduce
def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    db = [{'school_class': '4a', 'scores': [1,2,3,4,5]},           
          {'school_class': '5',  'scores': [4,3,4,2,3,5,4]},
          {'school_class': '5b', 'scores': [5,3,5,5,5,4,2]},
          {'school_class': '11', 'scores': [2,4,3]},
          {'school_class': '5a', 'scores': [3,3,4,3]}]
    av=[]
    for row in db:
        av=av+row['scores']
    print('Cредний балл по школе: ' , sum(av) / len(av))
    for row in db:
        print("В классе: {0} средний балл: {1}"
              .format (row['school_class'],
                       int(sum(row['scores'])/len(row['scores']))) )



    
if __name__ == "__main__":
    main()
