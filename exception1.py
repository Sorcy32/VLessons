"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

import time as t
def ask_user():
    """
    Замените pass на ваш код
    """
    dict={"Как дела":"Хорошо","Что делаешь?": "Программирую","Привет": "Здравствуй",
          "hi":"HELLo",'Что программируешь?':"Тебя",
          "Сколько времени?":str(t.strftime("Сейчас: %H:%M"))}
    while True:
        
        try:
            inp = input("Пользователь: ")
            answer=dict[inp]
            print('Программа: ' + dict[inp]) 
        except KeyboardInterrupt:
            print("Пока!")
            break
        except:
            print("Программа: Я не понимаю")
    
if __name__ == "__main__":
    ask_user()
        
