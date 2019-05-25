"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    db = [{'school_class': '4a', 'scores': [3,4,4,5,2]},           
          {'school_class': '5',  'scores': [2,4,5,5,3,4,5]},
          {'school_class': '5b', 'scores': [5,4,5,1,1,2,1]},
          {'school_class': '12', 'scores': [3,5,4,5,5,5,5]},
          {'school_class': '5a', 'scores': [5,4,5,1,2,2,1,2,4,5,5,5,5]},
          ]
    schoolClassesTotal=0
    schoolAverScores=0
    schoolSummOfAversByClasses=0
### ПЕРВЫМ нужно вывести средний балл по ШКОЛЕ. Считаем его и записываем в список средние по классам
    for clas in db:                                             #перебиваем классы
        aver=0
        classScoresTotal=0
        classStudentsTotal=0
        schoolClassesTotal+=1                                   #Попутно считаем сколько всего классов
        for score in clas['scores']:                            #перебираем оценки
            classScoresTotal+=round(score)
            classStudentsTotal+=1
            aver=int((round(classScoresTotal) / classStudentsTotal))
            clas["aver"]=aver                                   #Записываем в новое поле средний балл по классу
        schoolSummOfAversByClasses+=aver
    print("Средний балл по школе: " + str(int(schoolSummOfAversByClasses/schoolClassesTotal)))
    for clas in db:                                             #Пишем уже готовые 
        print("Средний балл по классу \"" + str(clas["school_class"]) + "\" = " + str(clas['aver']))

    
if __name__ == "__main__":
    main()
