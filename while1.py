"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user():
    """
    Замените pass на ваш код
    """
    answr=""
    while answr!="Хорошо":
        answr = input('Как дела? :')       
    print('OK')
    pass

    
if __name__ == "__main__":
    ask_user()
